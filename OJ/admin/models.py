from django.db import models, connection
from user.models import is_loggedin, get_user_id

# Create your models here.


def is_admin(handle):
    return handle == 'admin'


def add_contest_db():
    sql = """INSERT INTO OJ.CONTEST(CONTEST_ID , TITLE )
    VALUES(OJ.CONTEST_ID_SEQ.NEXTVAL , 'NEW CONTEST ' );"""

    with connection.cursor() as cursor:
        cursor.execute(sql)

    return
