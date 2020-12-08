from django.db import models
from django.db import connection

from OJ.utils import dictfetchall, get_random_number, get_current_time_sql, get_current_time
from admin.models import is_admin
from user.models import get_handle
from problem.models import get_owner_user_id, get_problems

from datetime import timedelta
# Create your models here.


def get_contest_clarifications_dict(contest_id):
    sql = """select *
    from oj.clarification
    where contest_id = %s
    order by PUBLISH_TIME DESC;"""
    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id])
        result = dictfetchall(cursor)
    return result


def get_writers(contest_id):
    sql = """ SELECT HANDLE , COLOR , USER_ID
    FROM OJ.MANAGER LEFT JOIN OJ.USERS USING (USER_ID) 
        LEFT JOIN OJ.RATING_DISTRIBUTION ON ( RATING BETWEEN MINIMUM_RATING AND MAXIMUM_RATING )
    WHERE CONTEST_ID = %s ;"""

    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id])
        result = dictfetchall(cursor)

    return result


def is_contest_running(start_time, duration):
    minutes = (get_current_time() - start_time).total_seconds()/60
    print('minute: ', minutes, 'duration', duration)
    return minutes >= 0 and minutes <= duration


def is_contest_upcoming(start_time):
    return (get_current_time() < start_time)


def get_contests_dict(user_id=None):
    sql = """SELECT CONTEST_ID , TITLE , START_TIME , DURATION , COUNT(USER_ID) AS TOTAL_PARTICIPANT
    FROM OJ.CONTEST LEFT JOIN OJ.PARTICIPANT USING (CONTEST_ID)
    GROUP BY CONTEST_ID , TITLE , START_TIME , DURATION 
    ORDER BY START_TIME + DURATION / 1440 DESC;"""

    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = dictfetchall(cursor)
        for contest in result:
            contest['WRITERS'] = get_writers(contest['CONTEST_ID'])

            if contest['START_TIME'] is None or contest['DURATION'] is None or is_contest_upcoming(contest['START_TIME']):
                contest['STATE'] = 'UPCOMING'
            elif is_contest_running(contest['START_TIME'], contest['DURATION']):
                contest['STATE'] = 'RUNNING'
            else:
                contest['STATE'] = 'ENDED'

            if user_id is not None:
                contest['REGISTERED'] = is_participant(
                    contest['CONTEST_ID'], user_id)
                contest['IS_MANAGER'] = is_admin(get_handle(
                    user_id)) or is_manager(contest['CONTEST_ID'], user_id)

            if contest['DURATION'] is not None:
                contest['DURATION_HOUR'] = contest['DURATION']//60
                contest['DURATION_MINUTE'] = contest['DURATION'] % 60
                contest['DURATION'] = timedelta(minutes=contest['DURATION'])

    return result


def get_problems_summary(contest_id):
    sql = """ SELECT ALIAS , PROBLEM_ID , PROBLEM_NAME  , TIMELIMIT , MEMORYLIMIT 
    FROM OJ.PROBLEM_CONTEST LEFT JOIN OJ.PROBLEM USING (PROBLEM_ID)
    WHERE CONTEST_ID = %s 
    ORDER BY ALIAS ASC;"""

    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id])
        result = dictfetchall(cursor)

    return result


def get_contest_dict(contest_id, user_id=None):
    sql = """ SELECT * 
    FROM OJ.CONTEST
    WHERE CONTEST_ID = %s ;"""

    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id])
        result = dictfetchall(cursor)[0]

    if result is not None:
        result['PROBLEMS'] = get_problems_summary(contest_id)
        result['WRITERS'] = get_writers(contest_id)
        result['CLARIFICATIONS'] = get_contest_clarifications_dict(contest_id)

        if result['START_TIME'] is None or result['DURATION'] is None or is_contest_upcoming(result['START_TIME']):
            result['STATE'] = 'UPCOMING'
        elif is_contest_running(result['START_TIME'], result['DURATION']):
            result['STATE'] = 'RUNNING'
        else:
            result['STATE'] = 'ENDED'

        result['IS_MANAGER'] = user_id is not None and is_manager(
            contest_id, user_id)
        if result['IS_MANAGER']:
            result['OWNER_PROBLEMS'] = get_problems(user_id)

    return result


def get_problem_id(contest_id, alias):
    sql = """ SELECT PROBLEM_ID 
    FROM OJ.PROBLEM_CONTEST
    WHERE CONTEST_ID = %s AND ALIAS = %s ;"""

    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id, alias])
        try:
            result = cursor.fetchone()[0]
        except:
            result = None

    return result


def add_participant(contest_id, user_id):
    sql = """INSERT INTO OJ.PARTICIPANT(CONTEST_ID , USER_ID)
    VALUES( %s , %s );"""
    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id, user_id])
    return


def remove_participant(contest_id, user_id):
    sql = """DELETE FROM OJ.PARTICIPANT
    WHERE CONTEST_ID = %s AND USER_ID = %s ;"""
    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id, user_id])
    return


def is_participant(contest_id,  user_id):
    """
    true if participant
    """
    sql = """SELECT COUNT(*)
    FROM OJ.PARTICIPANT
    WHERE CONTEST_ID = %s AND USER_ID = %s ;"""
    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id, user_id])
        result = cursor.fetchone()[0]
    return result == 1


def is_manager(contest_id,  user_id):
    """
    true/false if manager
    """
    sql = """SELECT COUNT(*)
    FROM OJ.MANAGER
    WHERE CONTEST_ID = %s AND USER_ID = %s ;"""
    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id, user_id])
        result = cursor.fetchone()[0]
    return result==1


def add_clarification_question(question, contest_id):
    """
    add new clarification
    """
    sql = f"""INSERT INTO OJ.CLARIFICATION(CLARIFICATION_ID,QUESTION ,PUBLISH_TIME,CONTEST_ID)
    VALUES (OJ.CLARIFICATION_ID_SEQ.NEXTVAL ,%s , { get_current_time_sql() } ,%s);"""
    with connection.cursor() as cursor:
        cursor.execute(sql, [question, contest_id])
    return


def remove_clarification_db(clarification_id, contest_id):
    sql = """delete from oj.clarification
    where clarification_id = %s 
    and contest_id = %s ;"""
    with connection.cursor() as cursor:
        cursor.execute(sql, [clarification_id, contest_id])
    return


def update_clarification(contest_id, clarification_id, answer):
    sql = """update oj.clarification
    set answer = %s 
    where clarification_id = %s 
    and contest_id = %s ;"""
    with connection.cursor() as cursor:
        cursor.execute(sql, [answer, clarification_id, contest_id])

    return


def add_problem_contest(contest_id, problem_id, alias):
    sql = """insert into oj.problem_contest(contest_id,problem_id,alias)
    values( %s , %s , %s );"""
    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id, problem_id, alias])
    return


def remove_problem_contest(contest_id, problem_id):
    sql = """delete from oj.PROBLEM_CONTEST
    where contest_id = %s   and problem_id = %s ;"""
    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id, problem_id])
    return


def get_standings_icpc_dict(contest_id):
    sql = """SELECT HANDLE , OJ.GET_RATING_COLOR(RATING) AS COLOR  ,
    SUM( NVL(ROUND((SUBMISSION_TIME - START_TIME ) * 24 * 60) , 0) ) AS TOTAL_TIME 
    FROM OJ.PARTICIPANT LEFT JOIN OJ.CONTEST USING (CONTEST_ID) 
    LEFT JOIN OJ.USERS USING ( USER_ID)
     LEFT JOIN OJ.SUBMISSION USING ( CONTEST_ID , USER_ID ) 
     LEFT JOIN OJ.PROBLEM_CONTEST USING (CONTEST_ID , PROBLEM_ID )
    WHERE CONTEST_ID = %s 
    GROUP BY HANDLE , RATING ;"""

    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id])
        result = dictfetchall(cursor)

    return result


def is_registered(contest_id , user_id ):
    """
    true/false
    """
    sql = """select count(*)
    from oj.PARTICIPANT 
    where contest_id = %s  and user_id = %s ;"""

    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id])
        result = cursor.fetchone()[0]

    return result == 1