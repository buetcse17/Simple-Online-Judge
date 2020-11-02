from django.db import models
from django.db import connection

from OJ.utils import log_sql
# Create your models here.


def AddFollower(followee_id, follower_id):
    """
        add to follow table
    """
    cursor = connection.cursor()
    sql = f'insert into oj.follow(followee_id , follower_id) values({followee_id} , {follower_id}) ;'

    cursor.execute(sql)
    log_sql(sql=sql)
    cursor.close()

    return


def RemoveFollower(followee_id, follower_id):
    """
        remove from follow table
    """
    cursor = connection.cursor()
    sql = f'delete from oj.follow where followee_id = {followee_id} and follower_id =  {follower_id} ;'

    cursor.execute(sql)
    log_sql(sql=sql)
    cursor.close()

    return
