from django.db import models
from django.db import connection

from OJ.utils import dictfetchall
# Create your models here.

def get_writers(contest_id ):
    sql = """ SELECT HANDLE , COLOR
    FROM OJ.MANAGER LEFT JOIN OJ.USERS USING (USER_ID) 
        LEFT JOIN OJ.RATING_DISTRIBUTION ON ( RATING BETWEEN MINIMUM_RATING AND MAXIMUM_RATING )
    WHERE CONTEST_ID = %s ;"""

    with connection.cursor() as cursor:
        cursor.execute(sql , [contest_id])
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


def get_contest_dict(contest_id):
    sql = """ select * 
    from oj.contest
    where contest_id = %s ;"""

    with connection.cursor() as cursor:
        cursor.execute(sql , [contest_id])
        result = dictfetchall(cursor)[0]

    return result