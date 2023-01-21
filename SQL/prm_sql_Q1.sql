show databases;
use  edy;
drop table if exists countries;
create  table countries(
COUNTRY_ID int,
COUNTRY_NAME varchar(15) ,
constraint check (COUNTRY_NAME in ('India','China','Italy')),
REGION_ID int
);
select * from countries;
-- Testing
insert into countries values( 12,'India',23);
insert into countries values( 13,'Italy',25);
insert into countries values( 14,'China',27);
insert into countries values( 15,'Peru',29); -- Error Code: 3819. Check constraint 'countries_chk_1' is violated.


