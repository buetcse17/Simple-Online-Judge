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

insert into oj.message(message_id , sender_id , receiver_id , text , time )             values( oj.message_id_seq.nextval , 6 , 5 , 'sdada' ,                  to_date( '2020-11-6-18-19-40'   , 'YYYY-MM-DD-HH24-MI-SS' )  ) ;
insert into oj.message(message_id , sender_id , receiver_id , text , time )             values( oj.message_id_seq.nextval , 5 , 6 , '12 31 am 12 7 2020' ,                  to_date( '2020-11-6-18-32-14'   , 'YYYY-MM-DD-HH24-MI-SS' )  ) ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
insert into oj.message(message_id , sender_id , receiver_id , text , time )             values( oj.message_id_seq.nextval , 5 , 6 , '<p><strong>ahsa sdf<em>gsdf</em></strong></p>' ,                  to_date( '2020-11-7-2-24-27'   , 'YYYY-MM-DD-HH24-MI-SS' )  ) ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
insert into oj.message(message_id , sender_id , receiver_id , text , time )             values( oj.message_id_seq.nextval , 5 , 6 , '<p>sdafa</p>' ,                  to_date( '2020-11-7-2-28-56'   , 'YYYY-MM-DD-HH24-MI-SS' )  ) ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
insert into oj.message(message_id , sender_id , receiver_id , text , time )             values( oj.message_id_seq.nextval , 5 , 6 , '<p>sdafa</p>' ,                  to_date( '2020-11-7-2-55-19'   , 'YYYY-MM-DD-HH24-MI-SS' )  ) ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
insert into oj.message(message_id , sender_id , receiver_id , text , time )             values( oj.message_id_seq.nextval , 5 , 6 , '<h1 style="text-align: justify;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Helllo&nbsp;</h1>' ,                  to_date( '2020-11-7-2-56-28'   , 'YYYY-MM-DD-HH24-MI-SS' )  ) ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
delete from oj.follow where followee_id = 6 and follower_id =  5 ;
insert into oj.follow(followee_id , follower_id) values(6 , 5) ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 ;
insert into oj.USERS(USER_ID, HANDLE, USER_NAME, EMAIL, PASSWORD_HASH )             values ( user_id_seq.nextval , %s , %s , %s , %s);
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 5 ;
insert into oj.message(message_id , sender_id , receiver_id , text , time )             values( oj.message_id_seq.nextval , 5 , 5 , '<p>asdasda</p>' ,                  to_date( '2020-11-7-5-13-53'   , 'YYYY-MM-DD-HH24-MI-SS' )  ) ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 5 ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 5 ;
delete from oj.follow where followee_id = 3 and follower_id =  5 ;
insert into oj.follow(followee_id , follower_id) values(3 , 5) ;
insert into oj.follow(followee_id , follower_id) values(4 , 5) ;
delete from oj.follow where followee_id = 4 and follower_id =  5 ;
insert into oj.follow(followee_id , follower_id) values(4 , 5) ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , %(sender_id)s , %(receiver_id)s , %(text)s ,                  to_date( '2020-11-7-5-37-46'  , 'YYYY-MM-DD-HH24-MI-SS' )  ) ;
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 ;
insert into oj.message(message_id , sender_id , receiver_id , text , time , attachment_location)             values( oj.message_id_seq.nextval , %(sender_id)s , %(receiver_id)s , %(text)s ,                 to_date( '2020-11-7-5-38-5'   , 'YYYY-MM-DD-HH24-MI-SS' ) ,                      %(attachment_location)s ) ;
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
update oj.message set seen = 1 where sender_id = 7 and receiver_id = 7 ;
update oj.message set seen = 1 where sender_id = 7 and receiver_id = 7 ;
update oj.message set seen = 1 where sender_id = 7 and receiver_id = 7 ;
update oj.message set seen = 1 where sender_id = 7 and receiver_id = 7 ;
update oj.message set seen = 1 where sender_id = 7 and receiver_id = 7 ;
insert into oj.USERS(USER_ID, HANDLE, USER_NAME, EMAIL, PASSWORD_HASH )             values ( user_id_seq.nextval , 'saomi' , 'Solaiman Ahmed' , '1705022@ugrad.buet.cse.ac.bd' , 'b3282a2f2a28757b3a18ab833de16a9c54518c0b0cf493e3f0a7cf09386f326a');
update oj.message set seen = 1 where sender_id = 7 and receiver_id = 7 ;
update oj.message set seen = 1 where sender_id = 7 and receiver_id = 7 ;
update oj.message set seen = 1 where sender_id = 7 and receiver_id = 7 ;
insert into oj.follow(followee_id , follower_id) values(3 , 7) ;
insert into oj.follow(followee_id , follower_id) values(5 , 7) ;
update oj.message set seen = 1 where sender_id = 7 and receiver_id = 7 ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 7 ;
insert into oj.message(message_id , sender_id , receiver_id , text , time )             values( oj.message_id_seq.nextval , 7 , 5 , '<p>Hello!!!</p>' ,                  to_date( '2020-11-7-3-48-23'   , 'YYYY-MM-DD-HH24-MI-SS' )  ) ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 7 ;
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 7 ;
insert into oj.message(message_id , sender_id , receiver_id , text , time , attachment_location)             values( oj.message_id_seq.nextval , %(sender_id)s , %(receiver_id)s , %(text)s ,                 to_date( '2020-11-7-5-39-36'   , 'YYYY-MM-DD-HH24-MI-SS' ) ,                      %(attachment_location)s ) ;
insert into oj.follow(followee_id , follower_id) values( 3 , 5 ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 5 , 6 , <p>বাংলা লিখা&nbsp;</p> ,                  to_date( '2020-11-7-8-51-35'  , 'YYYY-MM-DD-HH24-MI-SS' )  ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 5 , 6 , <p>হাহা&nbsp;</p> ,                  to_date( '2020-11-7-8-51-42'  , 'YYYY-MM-DD-HH24-MI-SS' )  ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 5 , 6 , <p>হাহা&nbsp;</p> ,                  to_date( '2020-11-7-8-55-31'  , 'YYYY-MM-DD-HH24-MI-SS' )  ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 5 , <p>dsadasdf&nbsp;</p> ,                  to_date( '2020-11-7-8-56-37'  , 'YYYY-MM-DD-HH24-MI-SS' )  ) 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 
insert into oj.country(country_id , country_name ) values(oj.country_id_seq.nextval , cntry )
 update oj.users set country_id = 201 where handle = abc 
 update oj.users set country_id = None where handle = abc 
 update oj.users set country_id = 201 where handle = abc 
 update oj.users set country_id = 201 where handle = abc 
 update oj.users set country_id = 201 where handle = abc 
 update oj.users set institution_id = 745 where handle = abc 
 update oj.users set country_id = 106 where handle = abc 
 update oj.users set institution_id = 745 where handle = abc 