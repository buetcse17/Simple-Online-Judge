from django.db import models , connection

# Create your models here.

def get_ratings():
   """
      list of tuple of ( handle , total_contest_participation , rating )
   """
   cursor = connection.cursor()
   sql = "SELECT oj.USERs.HANDLE , COUNT(oj.participant.contest_id) , oj.USERS.RATING \
FROM oj.users left join oj.participant ON (oj.USERS.USER_ID = oj.participant.USER_ID ) \
GROUP BY oj.users.USER_ID , oj.USERs.HANDLE , oj.USERS.RATING \
ORDER BY oj.USERS.RATING desc  , count(*) desc , oj.users.handle asc;"
   cursor.execute(sql)
   result = cursor.fetchall()
   cursor.close()
   return result


def get_country_ratings(country_id):
   """
      list of tuple of ( handle , total_contest_participation , rating )
   """
   cursor = connection.cursor()
   sql = f"SELECT oj.USERs.HANDLE , COUNT(oj.participant.contest_id) , oj.USERS.RATING \
FROM oj.users left join oj.participant ON (oj.USERS.USER_ID = oj.participant.USER_ID ) \
WHERE oj.USERS.country_id = {country_id}  \
GROUP BY oj.users.USER_ID , oj.USERs.HANDLE , oj.USERS.RATING \
ORDER BY oj.USERS.RATING desc  , count(*) desc , oj.users.handle asc;"
   cursor.execute(sql)
   result = cursor.fetchall()
   cursor.close()
   return result


def get_institution_ratings(institution_id):
   """
      list of tuple of ( handle , total_contest_participation , rating )
   """
   cursor = connection.cursor()
   sql = f"SELECT oj.USERs.HANDLE , COUNT(oj.participant.contest_id) , oj.USERS.RATING \
FROM oj.users left join oj.participant ON (oj.USERS.USER_ID = oj.participant.USER_ID ) \
WHERE oj.USERS.institution_id = {institution_id}  \
GROUP BY oj.users.USER_ID , oj.USERs.HANDLE , oj.USERS.RATING \
ORDER BY oj.USERS.RATING desc  , count(*) desc , oj.users.handle asc;"
   cursor.execute(sql)
   result = cursor.fetchall()
   cursor.close()
   return result

