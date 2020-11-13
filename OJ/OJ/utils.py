from message.models import get_total_new_messages


def log_sql(sql):
    f = open('log.sql','a' , encoding='utf-8')
    f.write( '\n' +sql )
    f.close()

def add_user_information(request  , context ):
    """
        Add total_new_messages to context
    """
    context['total_new_messages'] = get_total_new_messages(request.session['user_id'])
    return context

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]