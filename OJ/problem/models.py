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
    
    result['SAMPLE_TESTCASES'] = get_sample_testcases_dict(problem_id)

    # to_remove_key = [key for key , value in result.items() if value is None ]
    # for key in to_remove_key:
    #     del result[key]
    
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

    

    with connection.cursor() as cursor:
        cursor.execute(sql, post_data)


def get_testcases(problem_id):
    """
        testcase_id , input_file_location , output_file_location , problem_id
    """
    sql = """
        select testcase_id , input_file_location , output_file_location
        from oj.tastcase
        where problem_id = %s
        order by testcase_id; """
    with connection.cursor() as cursor:
        cursor.execute(sql, [problem_id])
        result = cursor.fetchall()

    return result

def add_testcase(problem_id, input_file_location, output_file_location):

    sql = """
        insert into oj.testcase( testcase_id, input_file_location, output_file_location, problem_id)
        values(oj.testcase_id_seq.nextval, %s, %s,%s); """
    
    with connection.cursor() as cursor:
        cursor.execute(sql, [input_file_location,output_file_location,problem_id])

    return

def get_testcase_problem_id(testcase_id):
    sql = """
        select problem_id
        from oj.testcase
        where testcase_id = %s ; """

    with connection.cursor() as cursor:
        cursor.execute(sql, [testcase_id])
        result = cursor.fetchone()[0]

    return result

def exist_testcase(testcase_id):
    sql ="""
        select count(*)
        from oj.testcase
        where testcase_id = %s ; """
    
    with connection.cursor() as cursor:
        cursor.execute(sql, [testcase_id])
        result = cursor.fetchone()[0]

    return result == 1

def get_testcase_dict(testcase_id):
    sql ="""
        select *
        from oj.testcase
        where testcase_id = %s ; """

    with connection.cursor() as cursor:
        cursor.execute(sql, [testcase_id])
        result = cursor.fetchone()[0]

    to_remove_key = [key for key , value in result.items() if value is None ]
    for key in to_remove_key:
        del result[key]

    return result

def update_testcase(post_data):
    sql = """
        update oj.testcase
        set input_file_location = %(INPUT_FILE_LOCATION)s,
            output_file_location = %(OUTPUT_FILE_LOCATION)s ,
            problem_id = %(PROBLEM_ID)s, 
        where testcase_id = %(TESTCASE_ID)s ; """

    
    with connection.cursor() as cursor:
        cursor.execute(sql, post_data)

    return



def get_sample_testcases_dict(problem_id):
    """
        *
    """
    sql = """SELECT *
        FROM OJ.SAMPLE_TESTCASE
        WHERE PROBLEM_ID = %s 
        ORDER BY SAMPLE_TESTCASE_ID;"""
    with connection.cursor() as cursor:
        cursor.execute(sql, [problem_id])
        result = dictfetchall(cursor)

    return result

def add_sample_testcase(post_data):

    sql = """insert into oj.sample_testcase
    values(
        %(SAMPLE_TESTCASE_ID)s ,
        %(INPUT)s ,
        %(OUTPUT)s ,
        %(PROBLEM_ID)s 
    );"""
    
    with connection.cursor() as cursor:
        cursor.execute(sql, post_data)

    return

def get_sample_testcase_problem_id(testcase_id):
    sql = """
        select problem_id
        from oj.sample_testcase
        where testcase_id = %s ; """

    with connection.cursor() as cursor:
        cursor.execute(sql, [testcase_id])
        result = cursor.fetchone()[0]

    return result

def exist_sample_testcase(testcase_id):
    sql ="""
        select count(*)
        from oj.sample_testcase
        where testcase_id = %s ; """
    
    with connection.cursor() as cursor:
        cursor.execute(sql, [testcase_id])
        result = cursor.fetchone()[0]

    return result == 1

def get_sample_testcase_dict(testcase_id):
    sql ="""
        select *
        from oj.sample_testcase
        where testcase_id = %s ; """

    with connection.cursor() as cursor:
        cursor.execute(sql, [testcase_id])
        result = cursor.fetchone()[0]

    to_remove_key = [key for key , value in result.items() if value is None ]
    for key in to_remove_key:
        del result[key]

    return result
