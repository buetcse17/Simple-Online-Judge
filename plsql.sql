create or replace procedure oj.sleep(sec in int) is
    v_now date;
begin
    select sysdate
    into v_now
    from DUAL;

    LOOP
        EXIT WHEN v_now + (sec * (1.0 / 86400)) <= SYSDATE;
    END LOOP;
end;
/
create or replace function oj.random_range(l in int, r in int) return int is -- [l,r]
    ret int ;
begin
    return round(DBMS_RANDOM.value * (r - l)) + l ;
end;
/


create or replace function oj.verdict_color(verdict in varchar2) return varchar2 as
begin
    if verdict like '%Accepted%' then
        return '#0a0';
    elsif verdict like '%Running%' or verdict like '%In Queue%' then
        return 'gray';
    elsif verdict like '%Wrong answer%' then
        return 'red';
    else
        return '#00a';
    end if;
end;
/

create or replace procedure oj.Update_Submission(submission_id_ in number, verdict_ in varchar2) is

begin
    update oj.SUBMISSION
    set VERDICT = verdict_
    where SUBMISSION_ID = submission_id_;
    commit;
end;

create or replace procedure oj.Run_Upto(submission_id_ in number, last_test in int) is
begin
    for i in 1..50
        loop
            Update_Submission(submission_id_, 'Running on test ' || i);
            oj.sleep(1);
            exit when i = last_test;
        end loop;
end;
/

create or replace procedure oj.Judge(submission_id_ in number) is
    pragma autonomous_transaction;
    fate      int ;
    i         int ;
    last_test int;
begin
    /*
    Accepted
    Wrong answer%
    Runtime error%
    Compilation error
    Time limit excedded%
    */
    fate := oj.random_range(0, 4);
    if fate = 0 then
        oj.RUN_UPTO(submission_id_, 51);
        Update_Submission(submission_id_, 'Accepted');
    elsif fate = 1 then
        last_test := oj.RANDOM_RANGE(1, 50);
        oj.RUN_UPTO(submission_id_, last_test);
        Update_Submission(submission_id_, 'Wrong answer on test ' || last_test);
    elsif fate = 2 then
        last_test := oj.RANDOM_RANGE(1, 50);
        oj.RUN_UPTO(submission_id_, last_test);
        Update_Submission(submission_id_, 'Runtime error on test ' || last_test);
    elsif fate = 3 then
        Update_Submission(submission_id_, 'Compilation error');
    elsif fate = 4 then
        last_test := oj.RANDOM_RANGE(1, 50);
        oj.RUN_UPTO(submission_id_, last_test);
        Update_Submission(submission_id_, 'Time limit exceeded on test ' || last_test);
    end if;
end;
/

create or replace trigger Fake_Judge
    after insert
    on oj.SUBMISSION
    for each row
declare
    SUBMISSION_ID_ number;
begin
    SUBMISSION_ID_ := :new.SUBMISSION_ID;
    --oj.JUDGE(SUBMISSION_ID_);
end;
/

begin
    oj.Judge(9553792635);
end;


create or replace function oj.get_rating_color(rating in number) return varchar2 is
    color_ varchar2(20) ;
begin
    select COLOR
    into color_
    from oj.RATING_DISTRIBUTION
    where rating between MINIMUM_RATING and MAXIMUM_RATING;
    return color_;
end;
/
