from django.db import models , connection

# Create your models here.

def get_ratings():
   """
      list of tuple of ( handle ,color , total_contest_participation , rating )
   """
   cursor = connection.cursor()
   sql = "SELECT oj.USERs.HANDLE ,oj.rating_distribution.color , COUNT(oj.participant.contest_id) , oj.USERS.RATING \
FROM oj.users left join oj.participant ON (oj.USERS.USER_ID = oj.participant.USER_ID ) \
   left join oj.rating_distribution on (oj.rating_distribution.minimum_rating <= oj.users.rating and oj.users.rating <= oj.rating_distribution.maximum_rating ) \
GROUP BY oj.users.USER_ID , oj.USERs.HANDLE , oj.USERS.RATING  ,oj.rating_distribution.color \
ORDER BY oj.USERS.RATING desc  , count(*) desc , oj.users.handle asc;"
   cursor.execute(sql)
   result = cursor.fetchall()
   cursor.close()
   return result


def get_country_ratings(country_id):
   """
      list of tuple of ( handle ,color , total_contest_participation , rating )
   """
   cursor = connection.cursor()
   sql = f"SELECT oj.USERs.HANDLE ,oj.rating_distribution.color, COUNT(oj.participant.contest_id) , oj.USERS.RATING \
FROM oj.users left join oj.participant ON (oj.USERS.USER_ID = oj.participant.USER_ID ) \
   left join oj.rating_distribution on (oj.rating_distribution.minimum_rating <= oj.users.rating and oj.users.rating <= oj.rating_distribution.maximum_rating ) \
WHERE oj.USERS.country_id = {country_id}  \
GROUP BY oj.users.USER_ID , oj.USERs.HANDLE , oj.USERS.RATING ,oj.rating_distribution.color \
ORDER BY oj.USERS.RATING desc  , count(*) desc , oj.users.handle asc;"
   cursor.execute(sql)
   result = cursor.fetchall()
   cursor.close()
   return result


def get_institution_ratings(institution_id):
   """
      list of tuple of ( handle ,color, total_contest_participation , rating )
   """
   cursor = connection.cursor()
   sql = f"SELECT oj.USERs.HANDLE ,oj.rating_distribution.color, COUNT(oj.participant.contest_id) , oj.USERS.RATING \
FROM oj.users left join oj.participant ON (oj.USERS.USER_ID = oj.participant.USER_ID ) \
   left join oj.rating_distribution on (oj.rating_distribution.minimum_rating <= oj.users.rating and oj.users.rating <= oj.rating_distribution.maximum_rating ) \
WHERE oj.USERS.institution_id = {institution_id}  \
GROUP BY oj.users.USER_ID , oj.USERs.HANDLE , oj.USERS.RATING  ,oj.rating_distribution.color \
ORDER BY oj.USERS.RATING desc  , count(*) desc , oj.users.handle asc;"
   cursor.execute(sql)
   result = cursor.fetchall()
   cursor.close()
   return result
def country_exists(country_id):
   """
      return true if country exists 
   """
   cursor = connection.cursor()
   sql = f"SELECT count(*) from oj.country where country_id = {country_id} ;"
   cursor.execute(sql)
   result = cursor.fetchone()[0]
   cursor.close()
   return result   != 0
def institution_exists(institution_id):
   """
      return true if institution exists 
   """
   cursor = connection.cursor()
   sql = f"SELECT count(*) from oj.institution where institution_id = {institution_id} ;"
   cursor.execute(sql)
   result = cursor.fetchone()[0]
   cursor.close()
   return result   != 0
