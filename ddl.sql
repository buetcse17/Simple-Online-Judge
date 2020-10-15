--- country table
drop table oj.COUNTRY;

CREATE TABLE OJ.COUNTRY
(
    country_id   INTEGER       not null,
    country_name VARCHAR2(100) NOT NULL,
    constraint PKCountry primary key (country_id)
);

--- institution table
drop table oj.Institution;

CREATE TABLE OJ.Institution
(
    Institution_id   INTEGER       not null,
    Institution_name VARCHAR2(100) NOT NULL,
    constraint PKInstitution primary key (Institution_id)
);

--- rating distribution table
drop table oj.Rating_Distribution;

create table oj.Rating_Distribution
(
    rating_catagory varchar2(20)
        constraint PKRating_Distribution primary key,
    minimum_rating  integer not null,
    maximum_rating  integer not null
);

--- users table
drop table oj.users;

create table oj.users
(
    user_id         integer      not null
        constraint PKUsers PRIMARY KEY,
    handle          varchar2(32) not null,
    user_name       varchar2(50) not null,
    email           varchar2(320),
    rating          integer default 0,
    password_hash   char(64)     not null,--- sha256.hexdigest()
    country_id      INTEGER,
    Institution_id  INTEGER,
    rating_catagory varchar2(20) not null,


    constraint FKCountry_id foreign key (country_id) references oj.country (country_id),
    constraint FKInstitution_id foreign key (Institution_id) references oj.Institution (Institution_id),
    constraint FKrating_catagory foreign key (rating_catagory) references oj.Rating_Distribution (rating_catagory)
);

--- Follow table
drop table oj.follow;
create table oj.Follow
(
    follower_id integer not null,
    followee_id integer not null,

    constraint FKFollower_id foreign key (follower_id) references oj.users (user_id),
    constraint FKFollowee_id foreign key (followee_id) references oj.users (user_id),
    constraint PKFollow primary key (followee_id, follower_id)
);

--- message table

create table oj.message
(
    message_id integer not null constraint PKMessage primary key ,
    file_location varchar2(512)  ,
    time date not null ,
    seen number(1) default 0,
    receiver_id integer      not null,
    sender_id integer      not null,
    constraint  FKSEnder_id foreign key (sender_id) references oj.users(user_id) ,
    constraint  FKreceiver_id foreign key (receiver_id) references oj.users(user_id)
);

create table  oj.problem(
    problem_id integer not null constraint PKProblem primary key ,
    name varchar2(100) not null ,
    description clob not null ,
    input_specification clob not null ,
    output_specification clob not null ,
    note clob not null ,
    timelimit integer not null ,
    memorylimit integer not null ,
    tutorial_link varchar2(2048)  ,
    difficulty integer ,
    owner_user_id         integer      not null ,
    constraint  FKUser_ID foreign key (owner_user_id) references oj.users(user_id)
);


--- Problem-CAtagory table

create  table oj.Problem_Catagory(
    problem_id integer not null,
    catagory_name varchar2(256) not null ,
    constraint PKProblem_Catagory primary key (problem_id , catagory_name ),
    constraint  FKProblem_id foreign key (problem_id) references oj.problem(problem_id)
);
