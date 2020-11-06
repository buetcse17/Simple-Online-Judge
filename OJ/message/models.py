from django.db import models
from django.db import connection
from django.utils import timezone

import OJ.utils
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

def add_message(sender_id , receiver_id ,text ,  attachment_location ):
    """
        add message to database 
    """
    time = timezone.now()
    print('year ' ,time.year)
    print('year ' ,time.month)
    print('year ' ,time.day)
    print('year ' ,time.hour)
    print('year ' ,time.minute)
    print('year ' ,time.second)

    print("now time: " , time)
    print("sender_id: " , sender_id)
    print("receiver_id: " , receiver_id)
    print("text: " , text)
    print("attachment_location: " , attachment_location)
    
    if len(text) == 0:
        text = ' '
    cursor = connection.cursor()
    if attachment_location is None :
        sql = f"insert into oj.message(message_id , sender_id , receiver_id , text , time ) \
            values( oj.message_id_seq.nextval , {sender_id} , {receiver_id} , '{text}' , \
                 to_date( '{time.year}-{time.month}-{time.day}-{time.hour}-{time.minute}-{time.second}'   , 'YYYY-MM-DD-HH24-MI-SS' )  ) ;"
    else :
        sql = f"insert into oj.message(message_id , sender_id , receiver_id , text , time , attachment_location) \
            values( oj.message_id_seq.nextval , {sender_id} , {receiver_id} , '{text}' , \
                to_date( '{time.year}-{time.month}-{time.day}-{time.hour}-{time.minute}-{time.second}'   , 'YYYY-MM-DD-HH24-MI-SS' ) ,  \
                    '{attachment_location}' ) ;"
    print(sql)
    cursor.execute(sql)
    OJ.utils.log_sql(sql)
    cursor.close()


    return 
