from django.db import models
from django.db import connection

# Create your models here.

def get_total_new_messages(user_id):
    """
        return total_new_messages from user_id
    """
    cursor = connection.cursor()
    sql = f"select count(distinct sender_id ) from oj.message where receiver_id = { user_id } and seen = 0 ;"
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    cursor.close()

    return result
