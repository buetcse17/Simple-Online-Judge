/*
table list in descending order of creation time

oj.contest_user_submission
oj.manager
oj.paricipant
oj.Problem_contest
oj.clarification
oj.contest
oj.submission
oj.sample_testcase
oj.testcase
oj.Problem_Catagory
oj.problem
oj.message
oj.Follow
oj.users
oj.Rating_Distribution
OJ.Institution
OJ.COUNTRY
 */

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'oj.contest_user_submission' ;
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'oj.manager' ;
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'oj.paricipant' ;
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'oj.Problem_contest';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'oj.clarification';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'oj.contest';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'oj.submission';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'oj.sample_testcase';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'oj.testcase';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'oj.Problem_Catagory';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'oj.problem';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'oj.message';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'oj.Follow';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'oj.users';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'oj.Rating_Distribution';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'OJ.Institution';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'OJ.COUNTRY';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;


--- country table

CREATE TABLE OJ.COUNTRY
(
    country_id   INTEGER       not null,
    country_name VARCHAR2(100) NOT NULL,
    constraint PKCountry primary key (country_id)
);

--- institution table


CREATE TABLE OJ.Institution
(
    Institution_id   INTEGER       not null,
    Institution_name VARCHAR2(100) NOT NULL,
    constraint PKInstitution primary key (Institution_id)
);

--- rating distribution table


create table oj.Rating_Distribution
(
    rating_catagory varchar2(20)
        constraint PKRating_Distribution primary key,
    minimum_rating  integer not null,
    maximum_rating  integer not null
);

--- users table


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
    constraint FKCountry_id foreign key (country_id) references oj.country (country_id) on delete set null ,
    constraint FKInstitution_id foreign key (Institution_id) references oj.Institution (Institution_id) on delete set null ,
    constraint FKrating_catagory foreign key (rating_catagory) references oj.Rating_Distribution (rating_catagory) on delete set null
);

--- Follow table

create table oj.Follow
(
    follower_id integer not null,
    followee_id integer not null,
    constraint FKFollower_id foreign key (follower_id) references oj.users (user_id) on delete cascade ,
    constraint FKFollowee_id foreign key (followee_id) references oj.users (user_id) on delete  cascade ,
    constraint PKFollow primary key (followee_id, follower_id)
);

--- message table

create table oj.message
(
    message_id    integer not null
        constraint PKMessage primary key,
    file_location varchar2(512),
    time          date    not null,
    seen          number(1) default 0,
    receiver_id   integer not null,
    sender_id     integer not null,
    constraint FKSEnder_id foreign key (sender_id) references oj.users (user_id) on delete cascade ,
    constraint FKreceiver_id foreign key (receiver_id) references oj.users (user_id) on delete cascade
);

create table oj.problem
(
    problem_id           integer       not null
        constraint PKProblem primary key,
    name                 varchar2(100) not null,
    description          clob          not null,
    input_specification  clob          not null,
    output_specification clob          not null,
    note                 clob          not null,
    timelimit            integer       not null,
    memorylimit          integer       not null,
    tutorial_link        varchar2(2048),
    difficulty           integer,
    owner_user_id        integer       not null,
    constraint FKUser_ID foreign key (owner_user_id) references oj.users (user_id) on delete cascade
);


--- Problem-Catagory table

create table oj.Problem_Catagory
(
    problem_id    integer       not null,
    catagory_name varchar2(256) not null,
    constraint PKProblem_Catagory primary key (problem_id, catagory_name),
    constraint FKProblem_id foreign key (problem_id) references oj.problem (problem_id) on delete cascade
);


--- TestCase table
create table oj.testcase
(
    testcase_id          integer        not null
        constraint PKTestcase primary key,
    input_file_location  varchar2(2048) not null,
    output_file_location varchar2(2048) not null,
    problem_id           integer        not null,
    constraint FKProblem_id_in_test_case foreign key (problem_id) references oj.problem (problem_id) on delete cascade
);

--- Sample Test Case Relation table

create table oj.sample_testcase
(
    problem_id  integer not null,
    testcase_id integer not null,
    constraint PKsample_testcase primary key (problem_id, testcase_id),
    constraint FKProblemid_sample_testcase foreign key (problem_id) references oj.problem (problem_id) on delete  cascade ,
    constraint FKtestcaseid_sample_testcase foreign key (testcase_id) references oj.testcase (testcase_id ) on delete cascade
);

--- submission table
create table oj.submission
(
    submission_id   integer not null
        constraint PKSubmission primary key,
    submission_time date    not null,
    judge_time      date,
    language        varchar2(128),
    execution_time  integer,
    memory_usages   integer,
    verdict         varchar2(32),
    raw_code        nclob   not null,
    problem_id      integer not null,
    constraint FKproblem_id_submission foreign key (problem_id) references oj.problem (problem_id) on delete cascade
);

--- contest table
create table oj.contest
(
    contest_id integer        not null
        constraint PKcontest primary key,
    title      nvarchar2(512) not null,
    start_time date,
    duration   integer
);

--- clarification table
create table oj.clarification
(
    clarification_id integer not null
        constraint PKclarification primary key,
    question         nclob   not null,
    answer           nclob   not null,
    publish_time     date,
    contest_id       integer not null,
    constraint FKcontest_clarification foreign key (contest_id) references oj.contest (contest_id) on delete cascade
);

create table oj.Problem_contest
(
    contest_id integer not null,
    problem_id integer not null,
    constraint PKProblem_contest primary key (contest_id, problem_id),
    constraint FKproblem_problemcontest foreign key (problem_id) references oj.problem (problem_id) on delete cascade ,
    constraint FKcontest_problemcontest foreign key (contest_id) references oj.contest (contest_id) on delete cascade
);

-- participant table
create table oj.paricipant
(
    contest_id integer not null,
    user_id    integer not null,
    constraint PKparticipant primary key (contest_id, user_id),
    constraint FKuser_participant foreign key (user_id) references oj.users (user_id) on delete cascade ,
    constraint FKcontest_participant foreign key (contest_id) references oj.contest (contest_id) on delete cascade
);

-- manager table
create table oj.manager
(
    contest_id integer not null,
    user_id    integer not null,
    constraint PKmanager primary key (contest_id, user_id),
    constraint FKuser_manager foreign key (user_id) references oj.users (user_id) on delete cascade ,
    constraint FKcontest_manager foreign key (contest_id) references oj.contest (contest_id) on delete cascade
);


-- contest_user_submission relation table

create table oj.contest_user_submission
(
    contest_id    integer not null,
    user_id       integer not null,
    submission_id integer not null,
    constraint PKcontest_user_submission primary key (contest_id, user_id, submission_id),
    constraint FKuser_contest_submission foreign key (user_id) references oj.users (user_id) on delete cascade ,
    constraint FKcontest_user_submission foreign key (contest_id) references oj.contest (contest_id) on delete cascade ,
    constraint FKsubmission_contest_user foreign key (submission_id) references oj.submission (submission_id) on delete cascade
);