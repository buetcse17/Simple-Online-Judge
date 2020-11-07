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
    sql = "select count(distinct sender_id ) from oj.message where receiver_id = %s and seen = 0 ;"
    cursor.execute(sql, [user_id])
    result = cursor.fetchone()[0]
    cursor.close()

    return result


def add_message(sender_id, receiver_id, text,  attachment_location):
    """
        add message to database 
    """
    time = timezone.now()
    """ print('year ' ,time.year)
    print('year ' ,time.month)
    print('year ' ,time.day)
    print('year ' ,time.hour)
    print('year ' ,time.minute)
    print('year ' ,time.second)

    print("now time: " , time)
    print("sender_id: " , sender_id)
    print("receiver_id: " , receiver_id)
    print("text: " , text)
    print("attachment_location: " , attachment_location) """

    if len(text) == 0:
        text = ' '
    cursor = connection.cursor()
    if attachment_location is None:
        sql = f"insert into oj.message(message_id , sender_id , receiver_id , text , time )  \
            values( oj.message_id_seq.nextval , %(sender_id)s , %(receiver_id)s , %(text)s , \
                 to_date( '{time.year}-{time.month}-{time.day}-{time.hour}-{time.minute}-{time.second}'  , 'YYYY-MM-DD-HH24-MI-SS' )  ) ;"

        data = {
            'sender_id': sender_id,
            'receiver_id': receiver_id,
            'text': text,
        }

    else:
        sql = f"insert into oj.message(message_id , sender_id , receiver_id , text , time , attachment_location) \
            values( oj.message_id_seq.nextval , %(sender_id)s , %(receiver_id)s , %(text)s , \
                to_date( '{time.year}-{time.month}-{time.day}-{time.hour}-{time.minute}-{time.second}'   , 'YYYY-MM-DD-HH24-MI-SS' ) ,  \
                    %(attachment_location)s ) ;"
        data = {
            'sender_id': sender_id,
            'receiver_id': receiver_id,
            'text': text,
            'attachment_location': attachment_location,
        }
    # print(sql)
    cursor.execute(sql, data)
    OJ.utils.log_sql(connection.queries[-1]['sql'])
    cursor.close()

    return


def set_seen_true(sender_id, receiver_id):
    """
    set seen 1 to all message between sender and receiver
    """

    sql = "update oj.message set seen = 1 where sender_id = %s and receiver_id = %s ;"
    cursor = connection.cursor()
    cursor.execute(sql, [sender_id, receiver_id])
    OJ.utils.log_sql(connection.queries[-1]['sql'])
    cursor.close()

    return


def get_messages_all(user_id):
    """
        sender_handle ,sender_color , receiver_handle , receiver_color , text , attachment  , time[sent] , seen 
    """

    sql = "select (select handle from oj.users where user_id  = sender_id ) as sender_handle ,\
            (select color from oj.Rating_Distribution where minimum_rating <= (select rating from oj.users where user_id = sender_id )  \
            and maximum_rating >= (select rating from oj.users where user_id = sender_id ) )  as sender_color ,  \
                (select handle from oj.users where user_id  = receiver_id ) as receiver_handle , \
            (select color from oj.Rating_Distribution where minimum_rating <= (select rating from oj.users where user_id = receiver_id )  \
            and maximum_rating >= (select rating from oj.users where user_id = receiver_id ) )  as receiver_color  ,\
                text  , attachment_location , time , seen \
     from oj.message where sender_id = %s or receiver_id = %s  order by time desc;"

    cursor = connection.cursor()
    cursor.execute(sql, [user_id, user_id])
    result = cursor.fetchall()
    cursor.close()

    return result


def get_messages_with(sender_id, receiver_id):
    """
        sender_handle ,sender_color , receiver_handle , receiver_color , text , attachment  , time[sent] , seen 
    """
    cursor = connection.cursor()
    sql = """
select (select handle from oj.users where user_id  = sender_id ) as sender_handle ,
        (select color 
        from oj.Rating_Distribution 
        where minimum_rating <= (select rating from oj.users where user_id = sender_id ) and maximum_rating >= (select rating from oj.users where user_id = sender_id ) 
        ) as sender_color ,  
        (select handle from oj.users where user_id  = receiver_id ) as receiver_handle , 
        (select color from oj.Rating_Distribution where minimum_rating <= (select rating from oj.users where user_id = receiver_id )  
                    and maximum_rating >= (select rating from oj.users where user_id = receiver_id ) )  as receiver_color  ,
        text  , attachment_location , time , seen 
from oj.message 
where sender_id in ( %(sender_id)s , %(receiver_id)s ) and receiver_id in ( %(receiver_id)s , %(sender_id)s ) 
order by time asc;"""

    cursor.execute(sql, {
        'sender_id': sender_id,
        'receiver_id': receiver_id,
    })
    result = cursor.fetchall()
    cursor.close()

    return result
