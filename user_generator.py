# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from faker import Faker
import hashlib
import random


def get_hash(password):
    """
        hashlib.sha256(password).hexdigest()
    """
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def to_sql(s):
    return '\'' + s.replace("'" , "''") + '\''

def get_institution():
    return random.randrange(2,8573)
def get_country():
    return random.randrange(2,197)
def get_rating():
    return random.randrange(100 , 2500)

def rearrange_str(s):
    x =list(s) 
    random.shuffle(x)
    return ''.join(x)

def rearrange_mail(mail):
    x = mail.split('@')
    return rearrange_str(x[0] ) + '@' + x[1]

def main():

    fil = open('gen.sql',mode='w')

    fake = Faker()
    n=int(input('total user:'))

    for _ in range(n):
        profile = fake.profile()
        #print(profile['username'])
        #print(profile['mail'])
        #print(to_sql(profile['name']))
        sql =f"""insert into oj.users(user_id ,
        handle ,
        user_name ,
        email ,
        rating ,
        PASSWORD_HASH,
        COUNTRY_ID ,
        INSTITUTION_ID )
        values(oj.user_id_seq.nextval ,
              {to_sql(rearrange_str(profile['username'])) } ,
              {to_sql(profile['name']) } ,
              {to_sql(rearrange_mail(profile['mail'])) } ,
              {get_rating()} ,
              {to_sql(get_hash('123'))} ,
              {get_country()},
              {get_institution()}
              );"""
        print(sql , file= fil)


if __name__ == '__main__':
    main()