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
    request.session['user_id'] = get_user_id(handle=handle)
    return


def logout(request):
    """
    docstring
    """
    try:
        del request.session['handle']
    except:
        pass
    try:
        del request.session['user_id']
    except:
        pass
    return


def is_loggedin(request):
    """
        return true if user is logged in
    """
    return 'handle' in request.session


def authenticate(handle, password_hash):
    """ 
        authenticate with handle and password_hash
        returns True if successful
        else returns False
    """
    cursor = connection.cursor()
    sql = "select count(*) from oj.users where handle = %s and password_hash = %s"
    cursor.execute(sql, [handle, password_hash])

    #print(sql.format(handle  , password_hash))
    print(connection.queries)

    result = cursor.fetchone()[0]
    print(handle, password_hash, result)
    return result == 1


def handle_exists(handle):
    """
        check if user exists with specific handle

    """
    cursor = connection.cursor()
    sql = "select count(*) from oj.users where handle = %s "
    cursor.execute(sql, [handle])
    result = cursor.fetchone()[0]
    #print(handle , result)
    return result == 1


def email_exists(email):
    """
        check if user exists with specific handle

    """
    cursor = connection.cursor()
    sql = "select count(*) from oj.users where email = %s "
    cursor.execute(sql, [email])
    result = cursor.fetchone()[0]
    print(email, result)
    return result == 1


def add_user(handle,  name, email, password_hash):
    """
        insert user into oj.users
    """
    print(handle,  name, email, password_hash)
    cursor = connection.cursor()
    result = False
    try:
        sql = f"insert into oj.USERS(USER_ID, HANDLE, USER_NAME, EMAIL, PASSWORD_HASH ) \
            values ( user_id_seq.nextval , '{handle}' , '{name}' , '{email}' , '{password_hash}');"
        cursor.execute(sql)
        print(sql)
        log_sql(sql)
        connection.commit()
        result = True

    except Exception as e:
        print(e)
    finally:
        cursor.close()
    return result


def get_hash(password):
    """
        hashlib.sha256(password).hexdigest()
    """
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def get_follower_count(user_id):
    """
        total follower 
    """
    cursor = connection.cursor()
    sql = f"select count(*) from oj.follow where followee_id = { user_id };"
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    cursor.close()
    return result


def get_user_id(handle):
    """
        get id from handle
    """
    cursor = connection.cursor()
    sql = f"select user_id from oj.users where handle = '{ handle }' ;"
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    cursor.close()
    return result


def get_user_information(handle):
    """
          user_id ,user_name ,   rating , rating_catagory ,color , country_id , country_name ,institution_id , institution_name , profile_picture_location
    """
    cursor = connection.cursor()
    sql = f"select oj.users.user_id ,  oj.users.user_name , oj.users.rating ,oj.rating_distribution.rating_catagory , oj.rating_distribution.color, oj.users.country_id , oj.country.country_name , \
        oj.users.Institution_id , oj.Institution.Institution_name  , oj.users.profile_picture_location \
     from oj.users left join oj.rating_distribution on (oj.rating_distribution.minimum_rating <= oj.users.rating and oj.users.rating <= oj.rating_distribution.maximum_rating ) \
     left join oj.country on (oj.users.country_id = oj.country.country_id ) \
         left join oj.institution on(oj.users.Institution_id =  oj.institution.Institution_id) \
             where oj.users.handle = '{handle}' ;"
    cursor.execute(sql)
    result = cursor.fetchone()

    # print(result)

    return result


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


def does_follow(followee_id, follower_id):
    """
        true if followee_id is followed by follower_id
    """

    cursor = connection.cursor()
    sql = f'select count(*) from oj.follow where followee_id = {followee_id} and follower_id = {follower_id} ;'
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    cursor.close()

    return result == 1


def update_profile_picture_location(handle, profile_picture_location):
    """
        update profile_picture_location in database
    """
    cursor = connection.cursor()
    sql = f"Update oj.users \
           SET profile_picture_location = '{profile_picture_location}'  \
               where handle = '{handle}' ;"
    cursor.execute(sql)
    log_sql(sql)
    cursor.close()

    return
