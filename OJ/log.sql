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
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 5 , 6 , <p>asda</p> ,                  to_date( '2020-11-8-10-41-55'  , 'YYYY-MM-DD-HH24-MI-SS' )  ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 5 , 6 , <p>haha</p> ,                  to_date( '2020-11-8-10-42-1'  , 'YYYY-MM-DD-HH24-MI-SS' )  ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 
insert into oj.USERS(USER_ID, HANDLE, USER_NAME, EMAIL, PASSWORD_HASH )             values ( user_id_seq.nextval , saomi , Solaiman Ahmed , 1705022@ugrad.buet.cse.ac.bd , b3282a2f2a28757b3a18ab833de16a9c54518c0b0cf493e3f0a7cf09386f326a)
 update oj.users set country_id = 15 where handle = saomi 
 update oj.users set institution_id = 624 where handle = saomi 
Update oj.users            SET profile_picture_location = codeforces.jpg                 where handle = saomi 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 5 , 6 , <p>fsafadfa</p> ,                  to_date( '2020-11-13-11-50-0'  , 'YYYY-MM-DD-HH24-MI-SS' )  ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
insert into oj.USERS(USER_ID, HANDLE, USER_NAME, EMAIL, PASSWORD_HASH )             values ( user_id_seq.nextval , qwe , abdbn asdjak , mahdi@gmail.com , a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3)
Update oj.users            SET profile_picture_location = pro pic_je0xpLX.png                 where handle = qwe 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 21 , 5 , <p>aksnbdfadsfa</p> ,                  to_date( '2020-11-14-6-7-5'  , 'YYYY-MM-DD-HH24-MI-SS' )  ) 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 21 
update oj.message set seen = 1 where sender_id = 21 and receiver_id = 5 
 update oj.users set country_id = 15 where handle = abc 
 update oj.users set institution_id = 600 where handle = abc 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 5 , 5 , <p>fasdfasdfa</p> ,                  to_date( '2020-11-16-4-49-49'  , 'YYYY-MM-DD-HH24-MI-SS' )  ) 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 5 
insert into oj.country(country_id , country_name ) values(oj.country_id_seq.nextval , bd )
 update oj.users set country_id = 201 where handle = qwe 
insert into oj.institution(institution_id , institution_name ) values(oj.institution_id_seq.nextval , buet )
 update oj.users set institution_id = 8581 where handle = qwe 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 5 , 5 , <p>sadfa</p> ,                  to_date( '2020-11-16-5-2-30'  , 'YYYY-MM-DD-HH24-MI-SS' )  ) 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 5 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 5 , 6 , <p>sdfasdfa</p> ,                  to_date( '2020-11-16-5-2-40'  , 'YYYY-MM-DD-HH24-MI-SS' )  ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 5 , 6 , <p>sfasxfa</p> ,                  to_date( '2020-11-16-9-35-8'  , 'YYYY-MM-DD-HH24-MI-SS' )  ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 6 , <p>sadasdfa</p> ,                  to_date( '2020-11-16-9-36-30'  , 'YYYY-MM-DD-HH24-MI-SS' )  ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 6 , <p>asdfafafa</p> ,                  to_date( '2020-11-16-9-36-35'  , 'YYYY-MM-DD-HH24-MI-SS' )  ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 
insert into oj.follow(followee_id , follower_id) values( 5 , 6 ) 
delete from oj.follow where followee_id = 5 and follower_id =  6 
insert into oj.follow(followee_id , follower_id) values( 5 , 6 ) 
insert into oj.USERS(USER_ID, HANDLE, USER_NAME, EMAIL, PASSWORD_HASH )             values ( user_id_seq.nextval , mahdi , Mahdi Hasnat Siyam , mahdibuet3@gmail.comasd , a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3)
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 1 , 1 , <p>fasdfa</p> ,                 to_date( '2020-11-17-12-10-23'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 1 and receiver_id = 1 
insert into oj.message(message_id , sender_id , receiver_id , text , time , attachment_location)             values( oj.message_id_seq.nextval , 1 , 1 , <p>asdfa</p> ,                  to_date( '2020-11-17-12-10-32'  , 'YYYY-MM-DD-HH24-MI-SS')  ,                      Class-lecture-Oct21-2020.mp4 ) 
update oj.message set seen = 1 where sender_id = 1 and receiver_id = 1 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 5 , 6 , <p>fasdfa</p> ,                 to_date( '2020-11-24-11-54-9'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 5 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
delete from oj.follow where followee_id = 6 and follower_id =  5 
insert into oj.follow(followee_id , follower_id) values( 6 , 5 ) 
 update oj.users set country_id = 77 where handle = abc 
 update oj.users set institution_id = 3142 where handle = abc 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 5 , <p>fasdfasdfa</p> ,                 to_date( '2020-11-27-15-0-5'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 5 , <p>fasdfasdfa</p> ,                 to_date( '2020-11-27-15-0-14'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 5 , <p>fasdfasdfa</p> ,                 to_date( '2020-11-27-15-7-11'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 5 , <p>asdasfda</p> ,                 to_date( '2020-11-27-15-7-16'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 5 , <p>sfasdfa</p> ,                 to_date( '2020-11-27-15-7-29'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 5 , <p>sfasdfa</p> ,                 to_date( '2020-11-27-15-8-28'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 5 , <p>fasdfa</p> ,                 to_date( '2020-11-27-15-9-36'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 5 , <p>asdfasdfa</p> ,                 to_date( '2020-11-27-15-10-29'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 5 , <p>sfasdfa</p> ,                 to_date( '2020-11-27-15-15-6'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 5 , <p>sdasfa</p> ,                 to_date( '2020-11-27-15-15-38'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 5 , <p>mahdi</p> ,                 to_date( '2020-11-27-15-15-53'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 6 , <p>asdfasdf</p> ,                 to_date( '2020-11-27-15-19-7'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 6 , <p>afsdfa</p> ,                 to_date( '2020-11-27-15-24-58'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 6 , <p>fasdfa</p> ,                 to_date( '2020-11-27-15-29-19'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 6 , <p>fasdfa</p> ,                 to_date( '2020-11-27-15-41-28'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 6 , <p>fasdfa</p> ,                 to_date( '2020-11-27-15-41-38'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 6 , <p>sdfasdfa</p> ,                 to_date( '2020-11-27-15-42-0'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 6 ,   ,                 to_date( '2020-11-27-15-42-3'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 6 ,   ,                 to_date( '2020-11-27-15-42-5'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 6 , <p>fasdfa</p> ,                 to_date( '2020-11-27-15-42-12'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 6 , <p>fasdfasdf</p> ,                 to_date( '2020-11-27-15-42-16'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 6 , <p>sdfasdfa</p> ,                 to_date( '2020-11-27-15-42-19'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 6 , <p>sdag bbjf baj bjkamg km,g ag</p> ,                 to_date( '2020-11-27-15-42-25'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 6 , <p>gasdgasdgasdgf</p> ,                 to_date( '2020-11-27-15-42-31'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 6 , <p>drop table;;</p>
<p>&nbsp;</p> ,                 to_date( '2020-11-27-15-42-40'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 6 , <p><strong>fasdfa</strong></p> ,                 to_date( '2020-11-27-15-42-52'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 6 , <p>dsfafasdfa</p> ,                 to_date( '2020-11-27-15-43-55'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 6 , <p>sdfasdfasdfa</p> ,                 to_date( '2020-11-27-15-43-59'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 6 , <p>fasdfasdfa</p> ,                 to_date( '2020-11-27-15-44-3'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 6 , <p>asdfasdfasdf</p> ,                 to_date( '2020-11-27-15-44-8'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 6 , <p>fasdfasdfa</p> ,                 to_date( '2020-11-27-21-51-32'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 6 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 5 and receiver_id = 6 
Update oj.users            SET profile_picture_location = pro pic_1N7motr.png                 where handle = admin 
insert into oj.follow(followee_id , follower_id) values( 30156 , 6 ) 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 6 , 30156 , <p>hey what's secret about ur rating ,huh</p> ,                 to_date( '2020-11-29-21-36-49'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 30156 and receiver_id = 6 
update oj.message set seen = 1 where sender_id = 30156 and receiver_id = 6 
insert into oj.USERS(USER_ID, HANDLE, USER_NAME, EMAIL, PASSWORD_HASH )             values ( user_id_seq.nextval , mahdi.hasnat , Mahdi Hasnat Siyam , mahdibuetdas3@gmail.com , a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3)
insert into oj.follow(followee_id , follower_id) values( 66981 , 6 ) 
insert into oj.USERS(USER_ID, HANDLE, USER_NAME, EMAIL, PASSWORD_HASH )             values ( user_id_seq.nextval , admin , admin , admin , admin@oj.com)
insert into oj.USERS(USER_ID, HANDLE, USER_NAME, EMAIL, PASSWORD_HASH )             values ( user_id_seq.nextval , abc , Mahdi Hasnat Siyam , mahdibuet3@gmail.com , a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3)
Update oj.users            SET profile_picture_location = pro pic_IMToXCR.png                 where handle = abc 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 836 , 836 , <p>fasfa</p> ,                 to_date( '2020-12-12-10-40-45'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 836 and receiver_id = 836 
insert into oj.message(message_id , sender_id , receiver_id , text , time )              values( oj.message_id_seq.nextval , 836 , 139 , <p>dsafa</p> ,                 to_date( '2020-12-12-10-40-56'  , 'YYYY-MM-DD-HH24-MI-SS') ) 
update oj.message set seen = 1 where sender_id = 139 and receiver_id = 836 
insert into oj.message(message_id , sender_id , receiver_id , text , time , attachment_location)             values( oj.message_id_seq.nextval , 836 , 139 , <p>solve this</p> ,                  to_date( '2020-12-12-10-41-8'  , 'YYYY-MM-DD-HH24-MI-SS')  ,                      CSE208-Jan-2020_ Branch and Bound_2.pdf ) 
update oj.message set seen = 1 where sender_id = 139 and receiver_id = 836 
update oj.message set seen = 1 where sender_id = 836 and receiver_id = 139 
insert into oj.message(message_id , sender_id , receiver_id , text , time , attachment_location)             values( oj.message_id_seq.nextval , 139 , 836 , <p>asfjkas</p> ,                  to_date( '2020-12-12-11-46-24'  , 'YYYY-MM-DD-HH24-MI-SS')  ,                      1705003.zip ) 
update oj.message set seen = 1 where sender_id = 836 and receiver_id = 139 
update oj.message set seen = 1 where sender_id = 139 and receiver_id = 836 