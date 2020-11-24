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


