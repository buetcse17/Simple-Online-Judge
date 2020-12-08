from django.utils import timezone
from datetime import datetime
from message.models import get_total_new_messages
import random


def log_sql(sql):
    f = open('log.sql', 'a', encoding='utf-8')
    f.write('\n' + sql)
    f.close()


def add_user_information(request, context):
    """
        Add total_new_messages to context
    """
    context['total_new_messages'] = get_total_new_messages(
        request.session['user_id'])
    return context


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def get_random_number(length):
    return random.randrange(9*10**(length-1), (10**length))


def get_time_sql(time):
    return f"to_date( '{time.year}-{time.month}-{time.day}-{time.hour}-{time.minute}-{time.second}'  , 'YYYY-MM-DD-HH24-MI-SS')"


def get_current_time():
    # time = timezone.now() #always utc
    # time = datetime.now()  # depennds on settings.py
    return datetime.now()


def get_current_time_sql():
    return get_time_sql(get_current_time())
