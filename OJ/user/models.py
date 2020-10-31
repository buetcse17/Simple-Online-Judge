from django.db import models
from django.db import connection
import hashlib


from OJ.utils import log_sql
# Create your models here.

def login(request, handle):
    """
    docstring
    """
    request.session['handle'] = handle
    return 
def logout(request):
    """
    docstring
    """
    try:
        del request.session['handle']
    except :
        pass
    return 
def authenticate(handle , password_hash):
    """ 
        authenticate with handle and password_hash
        returns True if successful
        else returns False
    """
    cursor  = connection.cursor()
    sql = "select count(*) from oj.users where handle = %s and password_hash = %s"
    cursor.execute(sql , [handle  , password_hash])
    
    #print(sql.format(handle  , password_hash)) 
    print(connection.queries)
    
    result = cursor.fetchone()[0]
    print(handle  , password_hash , result)
    return result == 1

def handle_exists(handle):
    """
        check if user exists with specific handle

    """
    cursor  = connection.cursor()
    sql = "select count(*) from oj.users where handle = %s "
    cursor.execute(sql , [handle ])
    result = cursor.fetchone()[0]
    #print(handle , result)
    return result == 1

def email_exists(email):
    """
        check if user exists with specific handle

    """
    cursor  = connection.cursor()
    sql = "select count(*) from oj.users where email = %s "
    cursor.execute(sql , [email ])
    result = cursor.fetchone()[0]
    print(email , result)
    return result == 1

def add_user(handle ,  name, email , password_hash):
    """
        insert user into oj.users
    """
    print(handle ,  name, email , password_hash)
    cursor = connection.cursor()
    result  = False 
    try :
        sql = f"insert into oj.USERS(USER_ID, HANDLE, USER_NAME, EMAIL, PASSWORD_HASH ) \
            values ( user_id_seq.nextval , '{handle}' , '{name}' , '{email}' , '{password_hash}');"
        cursor.execute(sql )
        print(sql)
        log_sql(sql)
        connection.commit()
        result = True 

    except Exception as e :
        print (e) 
    finally:
        cursor.close()
    return result


def get_hash(password ):
    """
        hashlib.sha256(password).hexdigest()
    """
    return hashlib.sha256(password.encode('utf-8')).hexdigest()
def get_follower_number( user_id ):
    """
        total follower 
    """
    cursor = connection.cursor()
    sql = f"select count(*) from oj.follow where followee_id = '{ user_id } ' ; "
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    cursor.close()
    return result

def get_user_id(handle ):
    """
        get id from handle
    """
    cursor = connection.cursor()
    sql = f"select user_id from oj.users where handle = '{ handle }' ;"
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    cursor.close()
    return result

def get_user_context( handle ):
    user_id = get_user_id(handle=handle)
    print(handle , user_id)
    pass

def get_country():
    """
        sql result of country_id , country_name
    """
    cursor = connection.cursor()
    sql = "select * from oj.country order by oj.country.country_name asc;"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return result
def get_institution():
    """
        sql result of institution_id , institution_name
    """
    cursor = connection.cursor()
    sql = "select * from oj.institution order by oj.institution.institution_name asc;"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return result