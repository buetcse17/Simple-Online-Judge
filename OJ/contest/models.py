from django.db import models
from django.db import connection

from OJ.utils import dictfetchall, get_random_number, get_current_time_sql
from admin.models import is_admin
from user.models import get_handle
# Create your models here.


def get_writers(contest_id):
    sql = """ SELECT HANDLE , COLOR , USER_ID
    FROM OJ.MANAGER LEFT JOIN OJ.USERS USING (USER_ID) 
        LEFT JOIN OJ.RATING_DISTRIBUTION ON ( RATING BETWEEN MINIMUM_RATING AND MAXIMUM_RATING )
    WHERE CONTEST_ID = %s ;"""

    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id])
        result = dictfetchall(cursor)

    return result


def get_contests_dict(user_id=None):
    sql = """SELECT CONTEST_ID , TITLE , START_TIME , DURATION , COUNT(USER_ID) AS TOTAL_PARTICIPANT
    FROM OJ.CONTEST LEFT JOIN OJ.PARTICIPANT USING (CONTEST_ID)
    GROUP BY CONTEST_ID , TITLE , START_TIME , DURATION 
    ORDER BY START_TIME DESC;"""

    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = dictfetchall(cursor)
        for contest in result:
            contest['WRITERS'] = get_writers(contest['CONTEST_ID'])
            contest['REGISTERED'] = is_participant(
                contest['CONTEST_ID'], user_id)
            contest['IS_MANAGER'] = is_admin(get_handle(
                user_id)) or is_manager(contest['CONTEST_ID'], user_id) == 1
            if contest['DURATION'] is not None:
                contest['DURATION_HOUR'] = contest['DURATION']//60
                contest['DURATION_MINUTE'] = contest['DURATION'] % 60
    return result


def get_problems_summary(contest_id):
    sql = """ SELECT ALIAS , PROBLEM_ID , PROBLEM_NAME  , TIMELIMIT , MEMORYLIMIT
    FROM OJ.PROBLEM_CONTEST LEFT JOIN OJ.PROBLEM USING (PROBLEM_ID)
    WHERE CONTEST_ID = %s ;"""

    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id])
        result = dictfetchall(cursor)

    return result


def get_contest_dict(contest_id):
    sql = """ SELECT * 
    FROM OJ.CONTEST
    WHERE CONTEST_ID = %s ;"""

    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id])
        result = dictfetchall(cursor)[0]

    if result is not None:
        result['PROBLEMS'] = get_problems_summary(contest_id)
        result['WRITERS'] = get_writers(result['CONTEST_ID'])

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
    1 if participant
    """
    sql = """SELECT COUNT(*)
    FROM OJ.PARTICIPANT
    WHERE CONTEST_ID = %s AND USER_ID = %s ;"""
    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id, user_id])
        result = cursor.fetchone()[0]
    return result


def is_manager(contest_id,  user_id):
    """
    1 if manager
    """
    sql = """SELECT COUNT(*)
    FROM OJ.MANAGER
    WHERE CONTEST_ID = %s AND USER_ID = %s ;"""
    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id, user_id])
        result = cursor.fetchone()[0]
    return result

def add_clarification_question(question ,publish_time ,contest_id):
    """
    add new clarification
    """
    sql = """INSERT INTO OJ.CLARIFICATION(CLARIFICATION_ID,QUESTION,PUBLISH_TIME,CONTEST_ID)
    VALUES (OJ.CLARIFICATION_ID_SEQ ,%s,%s,%s);"""
    with connection.cursor() as cursor:
        cursor.execute(sql , [question,publish_time,contest_id])
    return

def add_clarification_answer(clarification_id,answer):
    """
    """
    sql ="""update oj.clarification
    set answer = %s
    where clarification_id = %s;"""
    with connection.cursor() as cursor:
        cursor.execute(sql,[answer,clarification_id])
    return

def remove_clarification_db(clarification_id):
    sql ="""delete from oj.clarification
    where clarification_id = %s ;"""
    with connection.cursor() as cursor:
        cursor.execute(sql,[clarification_id])
    return

def get_clarification_question(clarification_id):
    sql = """select question
    from oj.clarification
    where clarification_id = %s ;"""
    with connection.cursor() as cursor:
        cursor.execute(sql,[clarification_id])
        result = cursor.fetchall()
    return result

def get_clarification_answer(clarification_id):
    sql = """select answer
    from oj.clarification
    where clarification_id = %s ;"""
    with connection.cursor() as cursor:
        cursor.execute(sql,[clarification_id])
        result = cursor.fetchall()
    return result

def get_contest_clarifications(contest_id):
    sql = """select clarification_id
    from oj.clarification
    where contest_id = %s;"""
    with connection.cursor() as cursor:
        cursor.execute(sql,[contest_id])
        result = cursor.fetchall()
    return result