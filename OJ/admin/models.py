from django.db import models, connection
from user.models import is_loggedin, get_user_id , handle_exists


from OJ.utils import get_time_sql
# Create your models here.


def is_admin(handle):
    return handle == 'admin'


def add_contest_db():
    sql = """INSERT INTO OJ.CONTEST(CONTEST_ID , TITLE )
    VALUES(OJ.CONTEST_ID_SEQ.NEXTVAL , 'NEW CONTEST ' );"""

    with connection.cursor() as cursor:
        cursor.execute(sql)

    return


def remove_contest_db(contest_id):
    sql = """delete from oj.contest
    where contest_id = %s ;"""

    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id])

    return


def update_contest_db(post_data):
    
    start_time = post_data['START_TIME'] # datetime object , none if null
    del post_data['START_TIME']
    manager_handle = post_data['MANAGER_HANDLE']
    del post_data['MANAGER_HANDLE']

    if start_time is None:
        sql = f"""UPDATE OJ.CONTEST
        SET TITLE = %(TITLE)s , 
            START_TIME = NULL ,
            DURATION = %(DURATION)s
        WHERE CONTEST_ID = %(CONTEST_ID)s ;"""
    else:
        sql = f"""UPDATE OJ.CONTEST
        SET TITLE = %(TITLE)s , 
            START_TIME = { get_time_sql(start_time) } ,
            DURATION = %(DURATION)s
        WHERE CONTEST_ID = %(CONTEST_ID)s ;"""
    print(manager_handle)
    if manager_handle is not None:
        if handle_exists(manager_handle) == True:
            manager_user_id = get_user_id(manager_handle)
            sql1 = f"""UPDATE OJ.MANAGER
            SET USER_ID = { manager_user_id }
            WHERE CONTEST_ID = %(CONTEST_ID)s ;
            """

    with connection.cursor() as cursor:
        cursor.execute(sql,post_data)
        cursor.execute(sql1,post_data)
    
    return 


def add_manager(contest_id, user_id):
    sql = """INSERT INTO OJ.MANAGER(CONTEST_ID , USER_ID)
    VALUES( %s , %s );"""
    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id, user_id])
    return


def remove_manager(contest_id, user_id):
    sql = """DELETE FROM OJ.MANAGER
    WHERE CONTEST_ID = %s AND USER_ID = %s ;"""
    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id, user_id])
    return

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

def get_manager(contest_id):
    """
    return the handle's of manager
    """
    sql = """SELECT * 
    FROM OJ.USER
    WHERE USER_ID = (SELECT USER_ID
    FROM OJ.MANAGER
    WHERE CONTEST_ID = %s
    ); """
    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id])
        result = cursor.fetchone()[0]
    return result



