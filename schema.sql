DROP DATABASE IF EXISTS entrytask; 
DROP DATABASE IF EXISTS luminus; 

CREATE DATABASE entrytask;
CREATE DATABASE luminus;

USE luminus;

DROP TABLE IF EXISTS View CASCADE;
DROP TABLE IF EXISTS Posts CASCADE;
DROP TABLE IF EXISTS Forums CASCADE;
DROP TABLE IF EXISTS Attendance CASCADE;
DROP TABLE IF EXISTS Attend CASCADE;
DROP TABLE IF EXISTS Assist CASCADE;
DROP TABLE IF EXISTS Facilitate CASCADE;
DROP TABLE IF EXISTS Tutorials CASCADE;
DROP TABLE IF EXISTS Teach CASCADE;
DROP TABLE IF EXISTS Enroll CASCADE;
DROP TABLE IF EXISTS Students CASCADE;
DROP TABLE IF EXISTS TAs CASCADE;
DROP TABLE IF EXISTS Participators CASCADE;
DROP TABLE IF EXISTS Admins CASCADE;
DROP TABLE IF EXISTS Courses CASCADE;
DROP TABLE IF EXISTS Profs CASCADE;
DROP TABLE IF EXISTS Users CASCADE;

create table Users (
uname varchar(50),
password varchar(256) not null,
name varchar (256) not null,
email varchar(256) not null,
last_login datetime(6),
PRIMARY KEY (uname)
);

create table Profs (
uname varchar(50),
expr integer,
FOREIGN KEY (uname) references Users(uname) ON DELETE CASCADE,
PRIMARY KEY (uname),
CHECK (expr >= 0)
);

create table Courses(
code varchar(50),
title varchar(200) not null,
info varchar(200),
lec_day varchar(20),
start_time  time,
end_time time,
PRIMARY KEY (code),
CHECK (lec_day= 'Mon' OR lec_day= 'Tue' OR lec_day= 'Wed' OR lec_day= 'Thur' OR lec_day= 'Fri')
);

create table Admins (
uname varchar(50),
FOREIGN KEY (uname) references Users(uname) ON DELETE CASCADE,
PRIMARY KEY (uname)
);

create table Participators(
uname varchar(50),
major varchar(50),
year integer,
matriculation_num varchar(50) UNIQUE not null,
FOREIGN KEY (uname) references Users(uname) ON DELETE CASCADE,
PRIMARY KEY (uname),
CHECK (year >= 1 AND year<= 5 AND length(matriculation_num)=9)
);

create table TAs(
uname varchar(50),
FOREIGN KEY (uname) references Participators(uname) ON DELETE CASCADE,
PRIMARY KEY (uname)
);

create table Students(
uname varchar(50),
FOREIGN KEY (uname) references Participators(uname) ON DELETE CASCADE,
PRIMARY KEY (uname)
);

create table Tutorials(
code varchar(50),
group_num varchar(50) not null,
tut_day varchar(20),
start_time time,
end_time time,
place varchar(50) not null,
FOREIGN KEY (code) references Courses(code) ON DELETE CASCADE,
PRIMARY KEY(code,group_num),
CHECK (tut_day = 'Mon' OR tut_day = 'Tue' OR tut_day = 'Wed' OR tut_day = 'Thur' OR tut_day = 'Fri')
);

create table Forums(
code varchar(50),
fid integer,
title varchar(255),
FOREIGN KEY (code) references Courses(code) ON DELETE CASCADE,
PRIMARY KEY(code, fid)
);

create table Posts(
code varchar(50),
fid integer,
pid integer,
t_code varchar(50),
t_fid integer,
t_pid integer,
uname varchar(50),
title  varchar(255),
content varchar(1027),
FOREIGN KEY (uname) references Users(uname) ON DELETE CASCADE,
FOREIGN KEY(code, fid) REFERENCES Forums(code, fid)  ON DELETE CASCADE,
FOREIGN KEY(t_code, t_fid, t_pid) REFERENCES Posts(code, fid, pid)  ON DELETE CASCADE,
PRIMARY KEY(code, fid, pid)
);

create table Assist(
uname varchar(50),
code varchar(50),
FOREIGN KEY (uname) references TAs(uname) ON DELETE CASCADE,
FOREIGN KEY (code) references Courses(code) ON DELETE CASCADE,
PRIMARY KEY(uname, code)
);

create table Facilitate(
uname varchar(50),
code varchar(50) not null,
group_num varchar(50) not null,
FOREIGN KEY (uname) references TAs(uname) ON DELETE CASCADE,
FOREIGN KEY (code,group_num) References Tutorials(code,group_num) ON DELETE CASCADE,
PRIMARY KEY(uname, code, group_num)
);

create table Attend(
uname varchar(50),
code varchar(50) ,
group_num varchar(50),
FOREIGN KEY (uname) references Students(uname) ON DELETE CASCADE,
FOREIGN KEY (code,group_num) References Tutorials(code,group_num) ON DELETE CASCADE,
PRIMARY KEY(uname, code)
);

create table Attendance(
uname varchar(50),
code varchar(50),
group_num varchar(50),
attend_week integer,
FOREIGN KEY (uname, code) References Attend(uname, code) ON DELETE CASCADE,
PRIMARY KEY(uname, code, attend_week)
);


create table Enroll(
uname varchar(50),
code varchar(50),
status varchar(50),
attendance_grade DECIMAL(6,3),
test_grade DECIMAL(6,3),
final_grade varchar(50), 
enroll_year YEAR,
FOREIGN KEY (uname) references Students(uname) ON DELETE CASCADE,
FOREIGN KEY (code) references Courses(code) ON DELETE CASCADE,
PRIMARY KEY (uname, code),
CHECK (status= 'enrolled' OR status= 'completed' OR status= 'rejected' OR status= 'requesting'),
CHECK (final_grade IS NULL OR (status ='completed' AND (final_grade= 'A' OR final_grade= 'B' OR final_grade= 'C' OR final_grade= 'D' OR final_grade= 'E' OR final_grade= 'F'))),
CHECK (enroll_year IS NULL OR (status= 'enrolled' OR status= 'completed'))
);

create table Teach (
uname varchar(50),
code varchar(50),
FOREIGN KEY (uname) references Profs(uname) ON DELETE CASCADE,
FOREIGN KEY (code) references Courses(code) ON DELETE CASCADE,
PRIMARY KEY (uname, code)
);

create table View(
f_code  varchar(50),
fid integer,
t_code varchar(50),
group_num varchar(50),
FOREIGN KEY (f_code,fid) references Forums (code, fid) ON DELETE CASCADE,
FOREIGN KEY (t_code,group_num) references Tutorials (code, group_num) ON DELETE CASCADE,
PRIMARY KEY (f_code, fid, t_code, group_num)
);


drop trigger if exists add_facilitate;
delimiter $$
create trigger add_facilitate before insert on Facilitate for each row 
begin
	call is_assist(NEW.uname, NEW.code);
end $$
delimiter ;

drop procedure if exists is_assist;
delimiter $$
create procedure is_assist(uname varchar(50), code varchar(50))
begin
declare count numeric;
declare message varchar(255);
select count(*) into count from Assist where uname = Assist.uname AND code = Assist.code;
if count=0 then
SET message = CONCAT('The TA is not assisting this course ', code);
 SIGNAL SQLSTATE '45000'  
SET MESSAGE_TEXT = message;
end if;
end $$ 
delimiter ;


drop trigger if exists add_assist;
delimiter $$
create trigger add_assist before insert on Assist for each row 
begin
	call check_assist_eligibility(NEW.uname, NEW.code);
end $$
delimiter ;

drop procedure if exists check_assist_eligibility;
delimiter $$
create procedure check_assist_eligibility(uname varchar(50), code varchar(50))
begin
declare count numeric;
declare message varchar(255);
select count(*) into count from Enroll e where 
uname = e.uname 
AND code = e.code
AND e.status = 'completed';
if count=0 then
SET message = CONCAT('The TA has not completed the course ', code);
 SIGNAL SQLSTATE '45000'  
SET MESSAGE_TEXT = message;
end if;
end $$ 
delimiter ;

drop trigger if exists add_attend;
delimiter $$
create trigger add_attend before insert on Attend for each row 
begin
	call check_enroll(NEW.uname, NEW.code);
end $$
delimiter ;

drop procedure if exists check_enroll;
delimiter $$
create procedure check_enroll(uname varchar(50), code varchar(50))
begin
declare count numeric;
declare message varchar(255);
select count(*) into count from Enroll e where 
uname = e.uname 
AND code = e.code
AND e.status = 'enrolled';
if count=0 then
SET message = CONCAT('The student is not enrolled in the course ', code);
 SIGNAL SQLSTATE '45000'  
SET MESSAGE_TEXT = message;
end if;
end $$ 
delimiter ;


drop trigger if exists add_attendance;
delimiter $$
create trigger add_attendance before insert on Attendance for each row 
begin
	call check_attend(NEW.uname, NEW.code,NEW.group_num);
end $$
delimiter ;

drop procedure if exists check_attend;
delimiter $$
create procedure check_attend(uname varchar(50), code varchar(50),group_num varchar(50))
begin
declare count numeric;
declare message varchar(255);
select count(*) into count from Attend a where 
uname = a.uname 
AND code = a.code
AND group_num = a.group_num;
if count=0 then
SET message = CONCAT('The student does not attend in the tut group ', group_num);
 SIGNAL SQLSTATE '45000'  
SET MESSAGE_TEXT = message;
else  update enroll e SET e.attendance_grade=e.attendance_grade+1 
where e.uname=uname;
end if;
end $$ 
delimiter ;




Insert into Users values('prof1', 'e10adc3949ba59abbe56e057f20f883e', 'Prof Ben', 'prof1@gmail.com',null);
Insert into Users values('prof2', 'e10adc3949ba59abbe56e057f20f883e', 'Prof Ken', 'prof2@gmail.com',null);
insert into Users values ('stu1', 'e10adc3949ba59abbe56e057f20f883e', 'Wang Xiaochao', 'stu1@gmail.com',null); 
insert into Users values ('stu2', 'e10adc3949ba59abbe56e057f20f883e', 'Chen Xiaoyun', 'stu2@gmail.com',null); 
insert into Users values ('stu3', 'e10adc3949ba59abbe56e057f20f883e', 'Chen Xiaoxi', 'stu3@gmail.com',null); 
insert into Users values ('stu4', 'e10adc3949ba59abbe56e057f20f883e', 'Chen Xiaojun', 'stu4@gmail.com',null); 
insert into Users values ('stu5', 'e10adc3949ba59abbe56e057f20f883e', 'Wang Dachao', 'stu5@gmail.com',null); 
insert into Users values ('stu6', 'e10adc3949ba59abbe56e057f20f883e', 'Huang Xiaoshuai', 'stu6@gmail.com',null); 
insert into Users values ('stu7', 'e10adc3949ba59abbe56e057f20f883e', 'Jack Cheong ', 'stu7@gmail.com',null); 
insert into Users values ('stu8', 'e10adc3949ba59abbe56e057f20f883e', 'Bob Tan', 'stu8@gmail.com',null); 
insert into Users values ('stu9', 'e10adc3949ba59abbe56e057f20f883e', 'Jack Teo', 'stu9@gmail.com',null); 
insert into Users values ('stu10', 'e10adc3949ba59abbe56e057f20f883e', 'Bryan He', 'stu10@gmail.com',null); 
insert into Users values ('stu11', 'e10adc3949ba59abbe56e057f20f883e', 'Tim Koh', 'stu11@gmail.com',null); 
insert into Users values ('stu12', 'e10adc3949ba59abbe56e057f20f883e', 'Alice Tan', 'stu12@gmail.com',null); 
insert into Users values ('stu13', 'e10adc3949ba59abbe56e057f20f883e', 'Stefanie Lim', 'stu13@gmail.com',null); 
insert into Users values ('stu14', 'e10adc3949ba59abbe56e057f20f883e', 'James Zhang', 'stu14@gmail.com',null); 
insert into Users values ('stu15', 'e10adc3949ba59abbe56e057f20f883e', 'Kyrie Yeong', 'stu15@gmail.com',null); 
insert into Users values ('stu16', 'e10adc3949ba59abbe56e057f20f883e', 'Kevin Cheong', 'stu16@gmail.com',null); 
insert into Users values ('stu17', 'e10adc3949ba59abbe56e057f20f883e', 'Clement Chong', 'stu17@gmail.com',null); 
insert into Users values ('stu18', 'e10adc3949ba59abbe56e057f20f883e', 'Harry Lim', 'stu18@gmail.com',null); 
insert into Users values ('stu19', 'e10adc3949ba59abbe56e057f20f883e', 'Curry Chan', 'stu19@gmail.com',null); 
insert into Users values ('stu20', 'e10adc3949ba59abbe56e057f20f883e', 'Evan Chua', 'stu20@gmail.com',null); 
insert into Users values ('ta1', 'e10adc3949ba59abbe56e057f20f883e', 'Jerry Cai', 'ta1@gmail.com',null); 
insert into Users values ('ta2', 'e10adc3949ba59abbe56e057f20f883e', 'Duke Goh', 'ta2@gmail.com',null); 
insert into Users values ('ta3', 'e10adc3949ba59abbe56e057f20f883e', 'Jack Chen', 'ta3@gmail.com',null); 
insert into Users values ('ta4', 'e10adc3949ba59abbe56e057f20f883e', 'Jasmine Yeo', 'ta4@gmail.com',null); 
insert into Users values ('ta5', 'e10adc3949ba59abbe56e057f20f883e', 'Daniel Chen', 'ta5@gmail.com',null); 




 
insert into participators values('stu1','IS',3,'a01712211');
insert into participators values('stu2','IS',3,'a01712111');
insert into participators values('stu3','IS',3,'a01711111');
insert into participators values('stu4','CS',3,'a01721111');
insert into participators values('stu5','CS',3,'a01731111');
insert into participators values('stu6','CS',3,'a01741111');
insert into participators values('stu7','CS',2,'a01751111');
insert into participators values('stu8','CS',1,'a01761111');
insert into participators values('stu9','CS',4,'a01771111');
insert into participators values('stu10','CS',5,'a01781111');
insert into participators values('stu11','IS',3,'a01781112');
insert into participators values('stu12','BA',1,'a01781113');
insert into participators values('stu13','CS',2,'a01781114');
insert into participators values('stu14','CS',3,'a01721222');
insert into participators values('stu15','CEG',4,'a01731112');
insert into participators values('stu16','CS',5,'a01741112');
insert into participators values('stu17','CS',4,'a01751112');
insert into participators values('stu18','CS',5,'a01761112');
insert into participators values('stu19','CS',5,'a01981112');
insert into participators values('stu20','CS',5,'a01791112');

insert into participators values('ta1','CS',5,'a01891111');
insert into participators values('ta2','CS',5,'a01891112');
insert into participators values('ta3','CS',5,'a01891113');
insert into participators values('ta4','CS',3,'a01891114');
insert into participators values('ta5','CS',4,'a01891115');


insert into Students values('stu1');
insert into Students values('stu2');
insert into Students values('stu3');
insert into Students values('stu4');
insert into Students values('stu5');
insert into Students values('stu6');
insert into Students values('stu7');
insert into Students values('stu8');
insert into Students values('stu9');
insert into Students values('stu10');
insert into Students values('stu11');
insert into Students values('stu12');
insert into Students values('stu13');
insert into Students values('stu14');
insert into Students values('stu15');
insert into Students values('stu16');
insert into Students values('stu17');
insert into Students values('stu18');
insert into Students values('stu19');
insert into Students values('stu20');
insert into Students values('ta1');
insert into Students values('ta2');
insert into Students values('ta3');
insert into Students values('ta4');
insert into Students values('ta5');

insert into TAs values('ta1');
insert into TAs values('ta2');
insert into TAs values('ta3');
insert into TAs values('ta4');
insert into TAs values('ta5');
insert into TAs values('stu1');

insert into Profs values('prof1',10);
insert into Profs values('prof2',10);

insert into Courses values ('cs2102', 'Database System', 'The aim of this module is to introduce the fundamental concept and techniques of relational database.', 'Mon', '16:00:00', '18:00:00');
insert into Courses values ('cs2103', 'Enterprise System Development', 'This module aims to train students to be conversant in backend or server-side development.', 'Tue', '14:00:00', '16:00:00');
insert into Courses values ('cs2104', 'Introduction to Operating Systems', 'This module introduces the basic concepts in operating systems and links it with contemporary operating system.', 'Wed', '8:00:00', '10:00:00');
insert into Courses values ('cs2105', 'Introduction to Computer Network', 'This module aims to provide a broad introduction to computer networks and network application programming.', 'Fri', '12:00:00', '14:00:00');
insert into Courses values ('cs2106', 'Research Methodology', 'Research methodology', 'Thur', '10:00:00', '12:00:00');
insert into Courses values ('cs2107', 'Introduction to Information Security', 'This module serves as an introductory module on information security.', 'Thur', '12:00:00', '14:00:00');


insert into Tutorials values ('cs2102', 'D01', 'Mon', '11:00:00', '12:00:00', 'i3-0339');
insert into Tutorials values ('cs2102', 'D02', 'Mon', '15:00:00', '16:00:00', 'i3-0338');
insert into Tutorials values ('cs2102', 'D03', 'Mon', '18:00:00', '19:00:00', 'i3-0337');
insert into Tutorials values ('cs2103', 'D01', 'Mon', '17:00:00', '18:00:00', 'i3-0335');
insert into Tutorials values ('cs2103', 'D02', 'Mon', '16:00:00', '17:00:00', 'i3-0333');
insert into Tutorials values ('cs2103', 'D03', 'Mon', '15:00:00', '16:00:00', 'com1-0113');
insert into Tutorials values ('cs2104', 'D01', 'Mon', '14:00:00', '15:00:00', 'com1-0113');
insert into Tutorials values ('cs2104', 'D02', 'Mon', '17:00:00', '19:00:00', 'com1-0113');
insert into Tutorials values ('cs2104', 'D03', 'Mon', '16:00:00', '18:00:00', 'com1-0113');
insert into Tutorials values ('cs2105', 'D01', 'Mon', '14:00:00', '15:00:00', 'com1-0113');
insert into Tutorials values ('cs2105', 'D02', 'Mon', '17:00:00', '19:00:00', 'com1-0113');
insert into Tutorials values ('cs2105', 'D03', 'Mon', '16:00:00', '18:00:00', 'com1-0113');


insert into Teach values('prof1', 'cs2102');
insert into Teach values('prof1', 'cs2103');
insert into Teach values('prof1', 'cs2104');
insert into Teach values('prof1', 'cs2105');



insert into enroll values('stu1', 'cs2102','enrolled', 0, 10, null, 2019);
insert into enroll values('stu2', 'cs2102','enrolled', 0, 15 , null, 2019);
insert into enroll values('stu3', 'cs2102','enrolled', 0, 20, null, 2019);
insert into enroll values('stu4', 'cs2102','enrolled', 0, 25, null, 2019);
insert into enroll values('stu5', 'cs2102','enrolled', 0, 30, null, 2019);
insert into enroll values('stu6', 'cs2102','enrolled', 0, 35, null, 2019);
insert into enroll values('stu7', 'cs2102','enrolled', 0, 40, null, 2019);
insert into enroll values('stu8', 'cs2102','enrolled', 0, 45, null, 2019);
insert into enroll values('stu9', 'cs2102','enrolled', 0, 50, null, 2019);
insert into enroll values('stu10', 'cs2102','enrolled', 0, 55, null, 2019);
insert into enroll values('stu11', 'cs2102','enrolled', 0, 60, null, 2019);
insert into enroll values('stu12', 'cs2102','enrolled', 0, 65, null, 2019);
insert into enroll values('stu13', 'cs2102','completed', 0, 70, 'A', 2019);
insert into enroll values('stu14', 'cs2102','completed', 0, 75, 'A', 2019);
insert into enroll values('stu15', 'cs2102','completed', 0, 80, null, 2019);
insert into enroll values('stu16', 'cs2102','completed', 0, 85, 'B', 2019);

insert into enroll values('stu1', 'cs2103','enrolled', 0, 0, null, 2019);
insert into enroll values('stu1', 'cs2105','rejected', 0, 0, null, null);

insert into enroll values('stu1', 'cs2104','completed', 0, 10, 'B', 2018);
insert into enroll values('stu2', 'cs2104','enrolled', 0, 15 , null, 2019);
insert into enroll values('stu3', 'cs2104','enrolled', 0, 20, null, 2019);
insert into enroll values('stu4', 'cs2104','enrolled', 0, 25, null, 2019);
insert into enroll values('stu5', 'cs2104','enrolled', 0, 30, null, 2019);


insert into enroll values('stu17', 'cs2102','requesting', 0, null, null, null);
insert into enroll values('stu18', 'cs2102','requesting', 0, null, null, null);


insert into enroll values('stu19', 'cs2102','rejected', 0, null, null, null);
insert into enroll values('stu20', 'cs2102','rejected', 0, null, null, null);

insert into enroll values('ta1', 'cs2102','completed', 10, 90, 'A', 2018);
insert into enroll values('ta2', 'cs2102','completed', 10, 70, 'B', 2018);
insert into enroll values('ta3', 'cs2102','completed', 10, 85,  'A', 2018);
insert into enroll values('ta4', 'cs2102','completed', 10, 80,  'B', 2018);
insert into enroll values('ta5', 'cs2102','completed', 10, 95,  'A', 2018);

insert into Attend values('stu1', 'cs2102', 'D01');
insert into Attend values('stu2', 'cs2102', 'D02');
insert into Attend values('stu3', 'cs2102', 'D03');
insert into Attend values('stu4', 'cs2102', 'D01');
insert into Attend values('stu5', 'cs2102', 'D02');
insert into Attend values('stu6', 'cs2102', 'D03');
insert into Attend values('stu7', 'cs2102', 'D01');
insert into Attend values('stu8', 'cs2102', 'D02');
insert into Attend values('stu9', 'cs2102', 'D03');

insert into Attend values('stu2', 'cs2104', 'D01');
insert into Attend values('stu3', 'cs2104', 'D01');
insert into Attend values('stu4', 'cs2104', 'D01');
insert into Attend values('stu5', 'cs2104', 'D01');

insert into Attendance values('stu1', 'cs2102', 'D01',1);
insert into Attendance values('stu2', 'cs2102', 'D02',1);
insert into Attendance values('stu3', 'cs2102', 'D03',1);
insert into Attendance values('stu4', 'cs2102', 'D01',1);
insert into Attendance values('stu5', 'cs2102', 'D02',1);
insert into Attendance values('stu6', 'cs2102', 'D03',1);
insert into Attendance values('stu7', 'cs2102', 'D01',1);
insert into Attendance values('stu8', 'cs2102', 'D02',1);
insert into Attendance values('stu9', 'cs2102', 'D03',1);

insert into Attendance values('stu3', 'cs2104', 'D01',1);
insert into Attendance values('stu3', 'cs2104', 'D01',2);
insert into Attendance values('stu3', 'cs2104', 'D01',3);
insert into Attendance values('stu4', 'cs2104', 'D01',1);
insert into Attendance values('stu5', 'cs2104', 'D01',1);

insert into assist values('ta1','cs2102');
insert into assist values('ta2','cs2102');
insert into assist values('ta3','cs2102');
insert into assist values('ta4','cs2102');
insert into assist values('ta5','cs2102');
insert into assist values('stu1','cs2104');

insert into Facilitate values('ta1', 'cs2102', 'D01' );
insert into Facilitate values('ta2', 'cs2102', 'D02' );
insert into Facilitate values('ta3', 'cs2102', 'D03' );

insert into Facilitate values('stu1', 'cs2104', 'D01' );
insert into Facilitate values('stu1', 'cs2104', 'D02' );

insert into Forums values('cs2102','1', 'cs2102 Forum 1');
insert into Forums values('cs2102','2', 'cs2102 Forum 2');
insert into Forums values('cs2102','3', 'cs2102 Forum 3');

insert into Forums values('cs2104','1', 'cs2104 Forum 1');
insert into Forums values('cs2104','2', 'cs2104 Forum 2');

Insert into view values('cs2102','1','cs2102','D01');
Insert into view values('cs2102','2','cs2102','D01');
Insert into view values('cs2102','2','cs2102','D02');
Insert into view values('cs2102','3','cs2102','D03');
Insert into view values('cs2104','1','cs2104','D01');

Insert into Posts values ('cs2102', 1, 1, null, null, null, 'stu1', '2102 Post 1', '2102 Content 1');
Insert into Posts values ('cs2102', 1, 2, 'cs2102', 1, 1, 'stu4', '2102 Reply 1', '2102 Reply Content 1');
Insert into Posts values ('cs2102', 1, 3, 'cs2102', 1, 1, 'stu7', '2102 Reply 2', '2102 Reply Content 2');
Insert into Posts values ('cs2102', 1, 4, 'cs2102', 1, 1, 'stu7', '2102 Reply 3', '2102 Reply Content 3');
Insert into Posts values ('cs2102', 1, 5, null, null, null, 'stu1', '2102 Post 2', '2102 Content 2');
Insert into Posts values ('cs2102', 1, 6, 'cs2102', 1, 5, 'stu4', '2102 Reply 4', '2102 Reply Content 4');
Insert into Posts values ('cs2102', 2, 1, null, null, null, 'stu1', '2102 Test Post 1', '2102 Test  Content 1');

Insert into Posts values ('cs2104', 1, 1, null, null, null, 'stu2', '2104 Post 1', '2104 Content 1');
Insert into Posts values ('cs2104', 1, 2, 'cs2104', 1, 1, 'stu3', '2104 Reply 1', '2104 Reply Content 1');
Insert into Posts values ('cs2104', 1, 3, 'cs2104', 1, 1, 'stu4', '2104 Reply 2', '2104 Reply Content 2');
Insert into Posts values ('cs2104', 1, 4, 'cs2104', 1, 1, 'stu5', '2104 Reply 3', '2104 Reply Content 3');
Insert into Posts values ('cs2104', 1, 5, null, null, null, 'stu4', '2104 Post 2', '2104 Content 2');
Insert into Posts values ('cs2104', 1, 6, 'cs2104', 1, 5, 'stu3', '2104 Reply 4', '2104 Reply Content 4');
Insert into Posts values ('cs2104', 2, 1, null, null, null, 'stu2', '2104 Test Post 1', '2104 Test  Content 1');