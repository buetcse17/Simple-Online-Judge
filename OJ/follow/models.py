from django.db import models
from django.db import connection

from OJ.utils import log_sql
# Create your models here.


def AddFollower(followee_id, follower_id):
    """
        add to follow table
    """
    cursor = connection.cursor()
    sql = 'insert into oj.follow(followee_id , follower_id) values( %s , %s ) ;'

    cursor.execute(sql, [followee_id, follower_id])
    log_sql(sql=sql)
    cursor.close()

    return


def RemoveFollower(followee_id, follower_id):
    """
        remove from follow table
    """
    cursor = connection.cursor()
    sql = 'delete from oj.follow where followee_id = %s and follower_id =  %s ;'

    cursor.execute(sql, [followee_id, follower_id])
    log_sql(sql=sql)
    cursor.close()

    return
