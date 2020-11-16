from django.db import models
from django.db import connection


from OJ.utils import dictfetchall
# Create your models here.


def get_problems(user_id):
    """
        problem_id , problem_name
    """
    sql = """
        select problem_id , problem_name 
        from oj.problem 
        where owner_user_id = %s 
        order by problem_id ;"""

    with connection.cursor() as cursor:
        cursor.execute(sql, [user_id])
        result = cursor.fetchall()

    return result


def add_problem(user_id):

    sql = """ insert into oj.problem( problem_id   , problem_name , description  ,  input_specification ,   output_specification ,
    note   ,timelimit  ,    memorylimit ,   owner_user_id  )
            values(oj.problem_id_seq.nextval , 'New problem' , 'Empty Description' ,'Empty Input Specification' , 'Empty Output Specification'  ,
    'Empty Node' , 1000 , 100000 , %s );"""

    with connection.cursor() as cursor:
        cursor.execute(sql, [user_id])

    return


def get_owner_user_id(problem_id):
    sql = """select owner_user_id 
    from oj.problem 
    where problem_id = %s ;"""

    with connection.cursor() as cursor:
        cursor.execute(sql, [problem_id])
        result = cursor.fetchone()[0]

    return result


def exist_problem(problem_id):
    sql = """select count(*)
    from oj.problem 
    where problem_id = %s ;"""

    with connection.cursor() as cursor:
        cursor.execute(sql, [problem_id])
        result = cursor.fetchone()[0]

    return result == 1


def get_problem_dict(problem_id):
    sql = """ select * 
    from oj.problem
    where problem_id = %s ;"""

    with connection.cursor() as cursor:
        cursor.execute(sql, [problem_id])
        result = dictfetchall(cursor)[0]
    

    to_remove_key = [key for key , value in result.items() if value is None ]
    for key in to_remove_key:
        del result[key]
    
    return result


def update_problem( post_data ):
    sql = """ UPDATE OJ.PROBLEM 
    SET PROBLEM_NAME  = %(PROBLEM_NAME)s ,
        DESCRIPTION   = %(DESCRIPTION)s ,
        INPUT_SPECIFICATION  = %(INPUT_SPECIFICATION)s ,
        OUTPUT_SPECIFICATION = %(OUTPUT_SPECIFICATION)s ,
        NOTE                 = %(NOTE)s ,
        TIMELIMIT           = %(TIMELIMIT)s ,
        MEMORYLIMIT         = %(MEMORYLIMIT)s ,
        TUTORIAL_LINK     = %(TUTORIAL_LINK)s ,
        DIFFICULTY =  %(DIFFICULTY)s 
    WHERE PROBLEM_ID = %(PROBLEM_ID)s ;"""

    print(type(post_data))
    print(post_data)

    with connection.cursor() as cursor:
        cursor.execute(sql, post_data)
