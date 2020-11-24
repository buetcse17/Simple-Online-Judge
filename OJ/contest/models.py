from django.db import models
from django.db import connection

from OJ.utils import dictfetchall, get_random_number, get_current_time_sql
# Create your models here.


def get_writers(contest_id):
    sql = """ SELECT HANDLE , COLOR
    FROM OJ.MANAGER LEFT JOIN OJ.USERS USING (USER_ID) 
        LEFT JOIN OJ.RATING_DISTRIBUTION ON ( RATING BETWEEN MINIMUM_RATING AND MAXIMUM_RATING )
    WHERE CONTEST_ID = %s ;"""

    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id])
        result = dictfetchall(cursor)

    return result


def get_contests_dict():
    sql = """SELECT CONTEST_ID , TITLE , START_TIME , DURATION , COUNT(USER_ID) AS TOTAL_PARTICIPANT
    FROM OJ.CONTEST LEFT JOIN OJ.PARTICIPANT USING (CONTEST_ID)
    GROUP BY CONTEST_ID , TITLE , START_TIME , DURATION 
    ORDER BY START_TIME DESC;"""

    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = dictfetchall(cursor)
        for contest in result:
            contest['WRITERS'] = get_writers(contest['CONTEST_ID'])

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

    return result


def exist_submission(submission_id):
    sql = """ SELECT COUNT(*) 
    FROM OJ.SUBMISSION
    WHERE SUBMISSION_ID = %s ;"""

    with connection.cursor() as cursor:
        cursor.execute(sql, [submission_id])
        result = cursor.fetchone()[0]

    return result == 1


def get_new_submission_id():

    submission_id = get_random_number(10)

    while exist_submission(submission_id):
        submission_id = get_random_number(10)

    return submission_id


def add_submission(post_data):

    # SUBMISSION_ID   INTEGER NOT NULL
    #     CONSTRAINT PKSUBMISSION PRIMARY KEY,
    # SUBMISSION_TIME DATE    NOT NULL,
    # JUDGE_TIME      DATE,
    # LANGUAGE        VARCHAR2(128),
    # EXECUTION_TIME  INTEGER,
    # MEMORY_USAGES   INTEGER,
    # VERDICT         VARCHAR2(32),
    # RAW_CODE        NCLOB   NOT NULL,
    # PROBLEM_ID      INTEGER NOT NULL,

    sql = f"""insert into oj.submission(
        SUBMISSION_ID , 
        SUBMISSION_TIME , 
        LANGUAGE ,
        VERDICT , 
        RAW_CODE ,
        PROBLEM_ID ,
        CONTEST_ID , 
        USER_ID
    )
    values(
        %(SUBMISSION_ID)s ,
        {get_current_time_sql()} , 
        %(LANGUAGE)s , 
        'In Queue' ,
        %(RAW_CODE)s ,
        %(PROBLEM_ID)s ,
        %(CONTEST_ID)s ,
        %(USER_ID)s

     );"""

    with connection.cursor() as cursor:
        cursor.execute(sql, post_data)

    return


def add_submission_to_contest(contest_id, user_id, submission_id):
    sql = """ insert into oj.contest_user_submission(
        contest_id , user_id , submission_id
    )
    values (
        %s , %s , %s
    );"""

    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id, user_id, submission_id])


def get_submissions_dict(contest_id):
    sql = """SELECT 
                    SUBMISSION_ID   ,
                    SUBMISSION_TIME ,
                    JUDGE_TIME      ,
                    LANGUAGE        ,
                    EXECUTION_TIME ,
                    MEMORY_USAGES  ,
                    VERDICT        ,
                    RAW_CODE        ,
                    PROBLEM_ID     ,
                    HANDLE        ,
                    CONTEST_ID  ,
                    PROBLEM_NAME ,
                    ALIAS 
    FROM OJ.SUBMISSION LEFT JOIN OJ.USERS USING (USER_ID)
            LEFT JOIN OJ.PROBLEM USING (PROBLEM_ID)
            LEFT JOIN OJ.PROBLEM_CONTEST USING(PROBLEM_ID , CONTEST_ID)
    WHERE CONTEST_ID = %s
    ORDER BY SUBMISSION_TIME DESC ;"""

    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id])
        result = dictfetchall(cursor)

    return result


def get_mysubmissions_dict(contest_id, user_id):
    sql = """SELECT 
                    SUBMISSION_ID   ,
                    SUBMISSION_TIME ,
                    JUDGE_TIME      ,
                    LANGUAGE        ,
                    EXECUTION_TIME ,
                    MEMORY_USAGES  ,
                    VERDICT        ,
                    RAW_CODE        ,
                    PROBLEM_ID     ,
                    HANDLE        ,
                    CONTEST_ID  ,
                    PROBLEM_NAME ,
                    ALIAS 
    FROM OJ.SUBMISSION LEFT JOIN OJ.USERS USING (USER_ID)
            LEFT JOIN OJ.PROBLEM USING (PROBLEM_ID)
            LEFT JOIN OJ.PROBLEM_CONTEST USING(PROBLEM_ID , CONTEST_ID)
    WHERE CONTEST_ID = %s AND USER_ID = %s
    ORDER BY SUBMISSION_TIME DESC ;"""

    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id, user_id])
        result = dictfetchall(cursor)

    return result


def get_submission_dict(submission_id):
    sql = """select * 
    from oj.submission LEFT JOIN OJ.USERS USING (USER_ID)
        LEFT JOIN OJ.PROBLEM USING (PROBLEM_ID)
        LEFT JOIN OJ.PROBLEM_CONTEST USING(PROBLEM_ID , CONTEST_ID)
    where submission_id = %s ;"""

    with connection.cursor() as cursor:
        cursor.execute(sql, [submission_id])
        result = dictfetchall(cursor)[0]
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


