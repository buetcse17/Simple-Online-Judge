/*
TABLE LIST IN DESCENDING ORDER OF CREATION TIME

OJ.CONTEST_USER_SUBMISSION
OJ.MANAGER
OJ.PARTICIPANT
OJ.PROBLEM_CONTEST
OJ.CLARIFICATION
OJ.CONTEST
OJ.SUBMISSION
OJ.SAMPLE_TESTCASE
OJ.TESTCASE
OJ.PROBLEM_CATAGORY
OJ.PROBLEM
OJ.MESSAGE
OJ.FOLLOW
OJ.USERS
OJ.RATING_DISTRIBUTION
OJ.INSTITUTION
OJ.COUNTRY

 */

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'OJ.CONTEST_USER_SUBMISSION' ;
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'OJ.MANAGER' ;
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'OJ.PARTICIPANT' ;
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'OJ.PROBLEM_CONTEST';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'OJ.CLARIFICATION';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'OJ.CONTEST';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'OJ.SUBMISSION';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'OJ.SAMPLE_TESTCASE';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'OJ.TESTCASE';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'OJ.PROBLEM_CATAGORY';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'OJ.PROBLEM';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'OJ.MESSAGE';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'OJ.FOLLOW';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'OJ.USERS';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'OJ.RATING_DISTRIBUTION';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE ' || 'OJ.INSTITUTION';
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

BEGIN
    EXECUTE IMMEDIATE 'DROP SEQUENCE ' || 'OJ.COUNTRY_ID_SEQ';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -2289 THEN
            RAISE;
        END IF;
END;
CREATE SEQUENCE OJ.COUNTRY_ID_SEQ ;

--- COUNTRY TABLE

CREATE TABLE OJ.COUNTRY
(
    COUNTRY_ID   INTEGER       NOT NULL,
    COUNTRY_NAME VARCHAR2(100) NOT NULL,
    CONSTRAINT PKCOUNTRY PRIMARY KEY (COUNTRY_ID) , 
    CONSTRAINT UNIQUECOUNTRY_NAME UNIQUE (COUNTRY_NAME)
);

BEGIN
    EXECUTE IMMEDIATE 'DROP SEQUENCE ' || 'OJ.INSTITUTION_ID_SEQ';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -2289 THEN
            RAISE;
        END IF;
END;
CREATE SEQUENCE OJ.INSTITUTION_ID_SEQ ;

--- INSTITUTION TABLE

CREATE TABLE OJ.INSTITUTION
(
    INSTITUTION_ID   INTEGER       NOT NULL,
    INSTITUTION_NAME VARCHAR2(100) NOT NULL,
    CONSTRAINT PKINSTITUTION PRIMARY KEY (INSTITUTION_ID) , 
    CONSTRAINT UNIQUEINSTITUTION_NAME UNIQUE (INSTITUTION_NAME )
);

--- RATING DISTRIBUTION TABLE

CREATE TABLE OJ.RATING_DISTRIBUTION
(
    RATING_CATAGORY VARCHAR2(20)
        CONSTRAINT PKRATING_DISTRIBUTION PRIMARY KEY,
    COLOR VARCHAR2(20) NOT NULL ,
    MINIMUM_RATING  INTEGER NOT NULL,
    MAXIMUM_RATING  INTEGER NOT NULL
);

BEGIN
    EXECUTE IMMEDIATE 'DROP SEQUENCE ' || 'OJ.USER_ID_SEQ';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -2289 THEN
            RAISE;
        END IF;
END;
CREATE SEQUENCE OJ.USER_ID_SEQ ;

--- USERS TABLE

CREATE TABLE OJ.USERS
(
    USER_ID         INTEGER       NOT NULL
        CONSTRAINT PKUSERS PRIMARY KEY,
    HANDLE          VARCHAR2(32)  NOT NULL,
    USER_NAME       VARCHAR2(50)  NOT NULL,
    EMAIL           VARCHAR2(320) NOT NULL,
    RATING          INTEGER DEFAULT 1500,
    PASSWORD_HASH   CHAR(64)      NOT NULL,--- SHA256.HEXDIGEST()
    COUNTRY_ID      INTEGER,
    INSTITUTION_ID  INTEGER,
    PROFILE_PICTURE_LOCATION VARCHAR2(512) DEFAULT 'NO-TITLE.JPG',
    ---RATING_CATAGORY VARCHAR2(20) , --- CAN BE OBTAINED BY QUERY
    CONSTRAINT UNIQUE_HANDLE UNIQUE (HANDLE),
    CONSTRAINT UNIQUE_EMAIL UNIQUE (EMAIL),
    CONSTRAINT FKCOUNTRY_ID FOREIGN KEY (COUNTRY_ID) REFERENCES OJ.COUNTRY (COUNTRY_ID) ON DELETE SET NULL,
    CONSTRAINT FKINSTITUTION_ID FOREIGN KEY (INSTITUTION_ID) REFERENCES OJ.INSTITUTION (INSTITUTION_ID) ON DELETE SET NULL,
    ---CONSTRAINT FKRATING_CATAGORY FOREIGN KEY (RATING_CATAGORY) REFERENCES OJ.RATING_DISTRIBUTION (RATING_CATAGORY) ON DELETE SET NULL ,
    CONSTRAINT CHECKHANDLE CHECK (HANDLE NOT LIKE '% %') ,
    CONSTRAINT CHECKEMAIL CHECK (EMAIL LIKE '%_@_%._%')
);

--- FOLLOW TABLE

CREATE TABLE OJ.FOLLOW
(
    FOLLOWER_ID INTEGER NOT NULL,
    FOLLOWEE_ID INTEGER NOT NULL,
    CONSTRAINT FKFOLLOWER_ID FOREIGN KEY (FOLLOWER_ID) REFERENCES OJ.USERS (USER_ID) ON DELETE CASCADE,
    CONSTRAINT FKFOLLOWEE_ID FOREIGN KEY (FOLLOWEE_ID) REFERENCES OJ.USERS (USER_ID) ON DELETE CASCADE,
    CONSTRAINT PKFOLLOW PRIMARY KEY (FOLLOWEE_ID, FOLLOWER_ID)
);


BEGIN
    EXECUTE IMMEDIATE 'DROP SEQUENCE ' || 'OJ.MESSAGE_ID_SEQ';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -2289 THEN
            RAISE;
        END IF;
END;
CREATE SEQUENCE OJ.MESSAGE_ID_SEQ ;

--- MESSAGE TABLE

CREATE TABLE OJ.MESSAGE
(
    MESSAGE_ID    INTEGER NOT NULL
        CONSTRAINT PKMESSAGE PRIMARY KEY,
    TEXT          CLOB    NOT NULL,
    ATTACHMENT_LOCATION VARCHAR2(512),
    TIME          DATE    NOT NULL,
    SEEN          NUMBER(1) DEFAULT 0,
    RECEIVER_ID   INTEGER NOT NULL,
    SENDER_ID     INTEGER NOT NULL,
    CONSTRAINT FKSENDER_ID FOREIGN KEY (SENDER_ID) REFERENCES OJ.USERS (USER_ID) ON DELETE CASCADE,
    CONSTRAINT FKRECEIVER_ID FOREIGN KEY (RECEIVER_ID) REFERENCES OJ.USERS (USER_ID) ON DELETE CASCADE
);

BEGIN
    EXECUTE IMMEDIATE 'DROP SEQUENCE ' || 'OJ.PROBLEM_ID_SEQ';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -2289 THEN
            RAISE;
        END IF;
END;
CREATE SEQUENCE OJ.PROBLEM_ID_SEQ ;

CREATE TABLE OJ.PROBLEM
(
    PROBLEM_ID           INTEGER       NOT NULL
        CONSTRAINT PKPROBLEM PRIMARY KEY,
    PROBLEM_NAME                 VARCHAR2(100) NOT NULL,
    DESCRIPTION          CLOB          NOT NULL,
    INPUT_SPECIFICATION  CLOB          NOT NULL,
    OUTPUT_SPECIFICATION CLOB          NOT NULL,
    NOTE                 CLOB          NOT NULL,
    TIMELIMIT            INTEGER       NOT NULL, --- MILISEC 
    MEMORYLIMIT          INTEGER       NOT NULL, --- KILOBYTE
    TUTORIAL_LINK        VARCHAR2(2048),
    DIFFICULTY           INTEGER,
    OWNER_USER_ID        INTEGER       NOT NULL,
    CONSTRAINT FKUSER_ID FOREIGN KEY (OWNER_USER_ID) REFERENCES OJ.USERS (USER_ID) ON DELETE CASCADE
);


--- PROBLEM-CATAGORY TABLE

CREATE TABLE OJ.PROBLEM_CATAGORY
(
    PROBLEM_ID    INTEGER       NOT NULL,
    CATAGORY_NAME VARCHAR2(256) NOT NULL,
    CONSTRAINT PKPROBLEM_CATAGORY PRIMARY KEY (PROBLEM_ID, CATAGORY_NAME),
    CONSTRAINT FKPROBLEM_ID FOREIGN KEY (PROBLEM_ID) REFERENCES OJ.PROBLEM (PROBLEM_ID) ON DELETE CASCADE
);

BEGIN
    EXECUTE IMMEDIATE 'DROP SEQUENCE ' || 'OJ.TESTCASE_ID_SEQ';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -2289 THEN
            RAISE;
        END IF;
END;
CREATE SEQUENCE OJ.TESTCASE_ID_SEQ ;

--- TESTCASE TABLE
CREATE TABLE OJ.TESTCASE
(
    TESTCASE_ID          INTEGER        NOT NULL
        CONSTRAINT PKTESTCASE PRIMARY KEY,
    INPUT_FILE_LOCATION  VARCHAR2(2048) NOT NULL,
    OUTPUT_FILE_LOCATION VARCHAR2(2048) NOT NULL,
    PROBLEM_ID           INTEGER        NOT NULL,
    CONSTRAINT FKPROBLEM_ID_IN_TESTCASE FOREIGN KEY (PROBLEM_ID) REFERENCES OJ.PROBLEM (PROBLEM_ID) ON DELETE CASCADE
);


--- SAMPLE TEST CASE RELATION TABLE

CREATE TABLE OJ.SAMPLE_TESTCASE
(
    TESTCASE_ID          INTEGER        NOT NULL
        CONSTRAINT PKSAMPLETESTCASE PRIMARY KEY,
    INPUT_FILE_LOCATION  VARCHAR2(2048) NOT NULL,
    OUTPUT_FILE_LOCATION VARCHAR2(2048) NOT NULL,
    PROBLEM_ID           INTEGER        NOT NULL,
    CONSTRAINT FKPROBLEMID_IN_SAMPLETESTCASE FOREIGN KEY (PROBLEM_ID) REFERENCES OJ.PROBLEM (PROBLEM_ID) ON DELETE CASCADE
);

BEGIN
    EXECUTE IMMEDIATE 'DROP SEQUENCE ' || 'OJ.SUBMISSION_ID_SEQ';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -2289 THEN
            RAISE;
        END IF;
END;
CREATE SEQUENCE OJ.SUBMISSION_ID_SEQ ;

--- SUBMISSION TABLE
CREATE TABLE OJ.SUBMISSION
(
    SUBMISSION_ID   INTEGER NOT NULL
        CONSTRAINT PKSUBMISSION PRIMARY KEY,
    SUBMISSION_TIME DATE    NOT NULL,
    JUDGE_TIME      DATE,
    LANGUAGE        VARCHAR2(128),
    EXECUTION_TIME  INTEGER,
    MEMORY_USAGES   INTEGER,
    VERDICT         VARCHAR2(32),
    RAW_CODE        NCLOB   NOT NULL,
    PROBLEM_ID      INTEGER NOT NULL,
    CONSTRAINT FKPROBLEM_ID_SUBMISSION FOREIGN KEY (PROBLEM_ID) REFERENCES OJ.PROBLEM (PROBLEM_ID) ON DELETE CASCADE
);


BEGIN
    EXECUTE IMMEDIATE 'DROP SEQUENCE ' || 'OJ.CONTEST_ID_SEQ';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -2289 THEN
            RAISE;
        END IF;
END;
CREATE SEQUENCE OJ.CONTEST_ID_SEQ ;

--- CONTEST TABLE
CREATE TABLE OJ.CONTEST
(
    CONTEST_ID INTEGER        NOT NULL
        CONSTRAINT PKCONTEST PRIMARY KEY,
    TITLE      NVARCHAR2(512) NOT NULL,
    START_TIME DATE,
    DURATION   INTEGER
);

BEGIN
    EXECUTE IMMEDIATE 'DROP SEQUENCE ' || 'OJ.CLARIFICATION_ID_SEQ';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -2289 THEN
            RAISE;
        END IF;
END;
CREATE SEQUENCE OJ.CLARIFICATION_ID_SEQ ;

--- CLARIFICATION TABLE
CREATE TABLE OJ.CLARIFICATION
(
    CLARIFICATION_ID INTEGER NOT NULL
        CONSTRAINT PKCLARIFICATION PRIMARY KEY,
    QUESTION         NCLOB   NOT NULL,
    ANSWER           NCLOB   NOT NULL,
    PUBLISH_TIME     DATE,
    CONTEST_ID       INTEGER NOT NULL,
    CONSTRAINT FKCONTEST_CLARIFICATION FOREIGN KEY (CONTEST_ID) REFERENCES OJ.CONTEST (CONTEST_ID) ON DELETE CASCADE
);

CREATE TABLE OJ.PROBLEM_CONTEST
(
    CONTEST_ID INTEGER NOT NULL,
    PROBLEM_ID INTEGER NOT NULL,
    ALIAS VARCHAR2(100) ,
    CONSTRAINT PKPROBLEM_CONTEST PRIMARY KEY (CONTEST_ID, PROBLEM_ID),
    CONSTRAINT FKPROBLEM_PROBLEMCONTEST FOREIGN KEY (PROBLEM_ID) REFERENCES OJ.PROBLEM (PROBLEM_ID) ON DELETE CASCADE,
    CONSTRAINT FKCONTEST_PROBLEMCONTEST FOREIGN KEY (CONTEST_ID) REFERENCES OJ.CONTEST (CONTEST_ID) ON DELETE CASCADE
);

-- PARTICIPANT TABLE
CREATE TABLE OJ.PARTICIPANT
(
    CONTEST_ID INTEGER NOT NULL,
    USER_ID    INTEGER NOT NULL,
    CONSTRAINT PKPARTICIPANT PRIMARY KEY (CONTEST_ID, USER_ID),
    CONSTRAINT FKUSER_PARTICIPANT FOREIGN KEY (USER_ID) REFERENCES OJ.USERS (USER_ID) ON DELETE CASCADE,
    CONSTRAINT FKCONTEST_PARTICIPANT FOREIGN KEY (CONTEST_ID) REFERENCES OJ.CONTEST (CONTEST_ID) ON DELETE CASCADE
);

-- MANAGER TABLE
CREATE TABLE OJ.MANAGER
(
    CONTEST_ID INTEGER NOT NULL,
    USER_ID    INTEGER NOT NULL,
    CONSTRAINT PKMANAGER PRIMARY KEY (CONTEST_ID, USER_ID),
    CONSTRAINT FKUSER_MANAGER FOREIGN KEY (USER_ID) REFERENCES OJ.USERS (USER_ID) ON DELETE CASCADE,
    CONSTRAINT FKCONTEST_MANAGER FOREIGN KEY (CONTEST_ID) REFERENCES OJ.CONTEST (CONTEST_ID) ON DELETE CASCADE
);


-- CONTEST_USER_SUBMISSION RELATION TABLE

CREATE TABLE OJ.CONTEST_USER_SUBMISSION
(
    CONTEST_ID    INTEGER NOT NULL,
    USER_ID       INTEGER NOT NULL,
    SUBMISSION_ID INTEGER NOT NULL,
    CONSTRAINT PKCONTEST_USER_SUBMISSION PRIMARY KEY (CONTEST_ID, USER_ID, SUBMISSION_ID),
    CONSTRAINT FKUSER_CONTEST_SUBMISSION FOREIGN KEY (USER_ID) REFERENCES OJ.USERS (USER_ID) ON DELETE CASCADE,
    CONSTRAINT FKCONTEST_USER_SUBMISSION FOREIGN KEY (CONTEST_ID) REFERENCES OJ.CONTEST (CONTEST_ID) ON DELETE CASCADE,
    CONSTRAINT FKSUBMISSION_CONTEST_USER FOREIGN KEY (SUBMISSION_ID) REFERENCES OJ.SUBMISSION (SUBMISSION_ID) ON DELETE CASCADE
);