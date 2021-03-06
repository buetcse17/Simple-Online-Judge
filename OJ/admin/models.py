from django.db import models, connection
from user.models import is_loggedin, get_user_id, handle_exists


from OJ.utils import get_time_sql
# Create your models here.


def is_admin(handle):
    """
    true/false
    """
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

    start_time = post_data['START_TIME']  # datetime object , none if null
    del post_data['START_TIME']

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

    with connection.cursor() as cursor:
        cursor.execute(sql, post_data)

    return


def add_manager(contest_id, user_id):
    sql = """INSERT INTO OJ.MANAGER(CONTEST_ID , USER_ID)
    VALUES( %s , %s );"""
    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id, user_id])
    return


def remove_manager_db(contest_id, user_id):
    sql = """DELETE FROM OJ.MANAGER
    WHERE CONTEST_ID = %s AND USER_ID = %s ;"""
    with connection.cursor() as cursor:
        cursor.execute(sql, [contest_id, user_id])
    return
