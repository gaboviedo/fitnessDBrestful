--  Sample exercise database 
--  See changelog table for details

DROP DATABASE IF EXISTS exercise;
CREATE DATABASE IF NOT EXISTS exercise;
USE exercise;
SELECT 'CREATING DATABASE STRUCTURE' as 'INFO';

DROP TABLE IF EXISTS exercise,
                     muscle_group,
                     ex_type,
                     weight,
                     preference,
                     user;


CREATE TABLE muscle_group (
    muscle_group_no int  PRIMARY KEY AUTO_INCREMENT,
    muscle_group_name   VARCHAR(25)     NOT NULL,
    upper       boolean         NOT NULL
)AUTO_INCREMENT = 1;

CREATE table preference(
    preference_no int primary key AUTO_INCREMENT,
    ex_type_no int,
    body_only boolean,
    level char(25)
);

CREATE table weight(
    weight_no int primary key AUTO_INCREMENT,
    user_no int,
    weight_pounds int,
    date_taken Date
);

CREATE TABLE ex_type (
    ex_type_no  int  PRIMARY KEY AUTO_INCREMENT,
    ex_type_name VARCHAR(25) NOT NULL
)AUTO_INCREMENT=1;
CREATE TABLE exercise (
    ex_no      mediumint PRIMARY KEY AUTO_INCREMENT,
    ex_title     VARCHAR(125)                NOT NULL,
    ex_desc     VARCHAR(1555)                NOT NULL,
    ex_type  VARCHAR(255)                    NOT NULL,
    muscle_group VARCHAR(255)                NOT NULL,
    equipment       CHAR(25)                 NOT NULL,
    level           char(25),
    rating         varchar(4),
    rating_desc     char(25)
);




CREATE TABLE user (
    user_no      int  AUTO_INCREMENT,
    user_name   VARCHAR(25)     NOT NULL,
    preference_no int,
   lessons_completed     INT         ,
   weight int,
   from_date    DATE            NOT NULL,
   primary key (user_no)
   )AUTO_INCREMENT=1;

SELECT 'LOADING exercise' as 'INFO';
source load_exercise.dump ;
SELECT 'LOADING ex_type' as 'INFO';
source load_extype.dump ;
SELECT 'LOADING muscle_group' as 'INFO';
source load_musclegroup.dump ;
SELECT 'LOADING user' as 'INFO';
source user.dump;
SELECT 'LOADING weight' as 'INFO';
source load_weight.dump;

select * from user where user.user_name = 'user0';
SELECT weight_pounds,date_taken,user_name,user.user_no from weight join (user) on user.user_no = weight.user_no;