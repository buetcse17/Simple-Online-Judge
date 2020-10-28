from django.db import models
from django.db import connection
import hashlib
# Create your models here.

def login(request, handle):
    """
    docstring
    """
    request.session['handle'] = handle
    return 
def logout(request, handle):
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
    print(handle , result)
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
        sql = "insert into oj.USERS(USER_ID, HANDLE, USER_NAME, EMAIL, PASSWORD_HASH ) \
                values ( user_id_seq.nextval , %s , %s , %s , %s )"
        cursor.execute(sql  , [ handle ,
                                 name  ,
                                 email  ,
                                password_hash  
                                ])
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