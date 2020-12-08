from django.db import models, connection
from OJ.utils import dictfetchall , get_current_time_sql
# Create your models here.

def get_all_problem_summury_dict():
    sql = f""" SELECT TO_CHAR(PROBLEM_ID) AS ALIAS , PROBLEM_ID, PROBLEM_NAME  , TIMELIMIT , MEMORYLIMIT
    FROM OJ.PROBLEM_CONTEST 
    left join oj.contest using(contest_id)
    LEFT JOIN OJ.PROBLEM USING (PROBLEM_ID)
    where (start_time + duration/60/24 ) <= { get_current_time_sql() }
    GROUP BY PROBLEM_ID ,  PROBLEM_NAME  , TIMELIMIT , MEMORYLIMIT ;"""

    with connection.cursor() as cursor :
        cursor.execute(sql)
        result = dictfetchall(cursor)
    
    return result