use  edy;
drop table if exists country_new;
create table country_new like countries;

alter table country_new
modify COUNTRY_ID varchar(2),
modify COUNTRY_NAME varchar(40),
modify REGION_ID decimal(10,0);

select * from country_new;