insert into oj.USERS(USER_ID, HANDLE, USER_NAME, EMAIL, PASSWORD_HASH )             values ( user_id_seq.nextval , 'rocky' , 'rocky' , 'rakibulhassanriaj@gmail.com' , '65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5');
insert into oj.USERS(USER_ID, HANDLE, USER_NAME, EMAIL, PASSWORD_HASH )             values ( user_id_seq.nextval , 'abchgjg' , 'Mahdi Hasnat Siyam' , 'mahdibuethhjhj3@gmail.com' , 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3' )
insert into oj.USERS(USER_ID, HANDLE, USER_NAME, EMAIL, PASSWORD_HASH )             values ( user_id_seq.nextval , 'klfsjaifojp' , 'Mahdi Hasnat Siyam' , 'mahdibueadasdat3@gmail.com' , 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3');
insert into oj.USERS(USER_ID, HANDLE, USER_NAME, EMAIL, PASSWORD_HASH )             values ( user_id_seq.nextval , 'abc' , 'Mahdi Hasnat Siyam' , 'mahdibuet3@gmail.com' , 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3');
insert into oj.USERS(USER_ID, HANDLE, USER_NAME, EMAIL, PASSWORD_HASH )             values ( user_id_seq.nextval , 'mahdi.hasnat' , 'Mahdi Hasnat Siyam' , 'mahdibuet3@gmail.comdasa' , 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3');
insert into oj.follow(followee_id , follower_id) values(6 , 5) ;
delete from oj.follow where followee_id = 6 and follower_id =  5 ;
insert into oj.follow(followee_id , follower_id) values(6 , 5) ;
delete from oj.follow where followee_id = 6 and follower_id =  5 ;
insert into oj.follow(followee_id , follower_id) values(6 , 5) ;
delete from oj.follow where followee_id = 6 and follower_id =  5 ;
insert into oj.follow(followee_id , follower_id) values(3 , 5) ;
delete from oj.follow where followee_id = 3 and follower_id =  5 ;
insert into oj.follow(followee_id , follower_id) values(3 , 5) ;
delete from oj.follow where followee_id = 3 and follower_id =  5 ;
insert into oj.follow(followee_id , follower_id) values(3 , 5) ;
delete from oj.follow where followee_id = 3 and follower_id =  5 ;
insert into oj.follow(followee_id , follower_id) values(3 , 5) ;
delete from oj.follow where followee_id = 3 and follower_id =  5 ;
insert into oj.follow(followee_id , follower_id) values(6 , 5) ;
insert into oj.follow(followee_id , follower_id) values(2 , 5) ;
insert into oj.follow(followee_id , follower_id) values(3 , 5) ;
Update oj.users            SET profile_picture_location = 'pro pic.png'                 where handle = 'abc' ;
Update oj.users            SET profile_picture_location = 'pro pic_lLA5K1E.png'                 where handle = 'abc' ;
insert into oj.message(message_id , sender_id , receiver_id , text , time )             values( oj.message_id_seq.nextval , 5 , 6 , 'help' , (select systimestamp at time zone 'UTC' from dual)  ) ;
insert into oj.message(message_id , sender_id , receiver_id , text , time )             values( oj.message_id_seq.nextval , 5 , 4 , 'mahdi' ,                  to_date( '2020-11-6-7-1-35'   , 'YYYY-MM-DD-HH24-MI-SS' )  ) ;
insert into oj.message(message_id , sender_id , receiver_id , text , time , attachment_location)             values( oj.message_id_seq.nextval , 5 , 6 , 'sdafa' ,                 to_date( '2020-11-6-16-0-51'   , 'YYYY-MM-DD-HH24-MI-SS' ) ,                      'wavelet tree paper_xBhAlxH.pdf' ) ;
insert into oj.message(message_id , sender_id , receiver_id , text , time )             values( oj.message_id_seq.nextval , 5 , 6 , 'fasdfa' ,                  to_date( '2020-11-6-17-9-39'   , 'YYYY-MM-DD-HH24-MI-SS' )  ) ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 ;
insert into oj.message(message_id , sender_id , receiver_id , text , time )             values( oj.message_id_seq.nextval , 6 , 5 , 'sdada' ,                  to_date( '2020-11-6-18-19-40'   , 'YYYY-MM-DD-HH24-MI-SS' )  ) ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 5 ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
insert into oj.message(message_id , sender_id , receiver_id , text , time )             values( oj.message_id_seq.nextval , 5 , 6 , '12 31 am 12 7 2020' ,                  to_date( '2020-11-6-18-32-14'   , 'YYYY-MM-DD-HH24-MI-SS' )  ) ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 ;