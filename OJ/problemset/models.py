from django.db import models, connection
from OJ.utils import dictfetchall
# Create your models here.

def get_all_problem_summury_dict():
    sql = """ SELECT TO_CHAR(PROBLEM_ID) AS ALIAS , PROBLEM_ID, PROBLEM_NAME  , TIMELIMIT , MEMORYLIMIT
    FROM OJ.PROBLEM_CONTEST LEFT JOIN OJ.PROBLEM USING (PROBLEM_ID)
    GROUP BY PROBLEM_ID ,  PROBLEM_NAME  , TIMELIMIT , MEMORYLIMIT ;"""

    with connection.cursor() as cursor :
        cursor.execute(sql)
        result = dictfetchall(cursor)
    
    return result