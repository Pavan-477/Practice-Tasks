create DATABASE EDY;
use EDY;

create TABLE SalesPeople(
Snum int primary key,
Sname varchar(15) unique,
City varchar(15),
Comm int
);

INSERT INTO SalesPeople values
(1001,'Peel', 'London' ,12),
(1002, 'Serres','Sanjose ',13),
(1004,'Motika','London',11),
(1007, 'Rifkin','Barcelona',15),
(1003,'Axelrod','Newyork',10)
;

create Table Customers(
Cnum int primary key,
Cname varchar(15),
City varchar(15) not null,
Snum int,
foreign key(snum) references salespeople(snum)
);
INSERT INTO Customers VALUES
(2001 , 'Hoffman',' London' ,1001),
(2002 , 'Giovanni', 'Rome' ,1003),
(2003 , 'Liu', 'Sanjose' ,1002),
(2004 , 'Grass' ,'Berlin' ,1002),
(2006 ,'Clemens',' London', 1001),
(2008 ,'Cisneros' ,'Sanjose ',1007),
(2007 ,'Pereira ','Rome ',1004);


Create Table  Orders(
Onum int primary key,
Amt double,
Odate varchar(11) ,
Cnum int,
foreign key(cnum) references customers(cnum),
Snum int,
foreign key(snum) references salespeople(snum)
);

INSERT INTO Orders VALUES
(3001,18.69,'3-10-1990' ,2008,1007),
(3003,767.19,'3-10-1990',2001,1001),
(3002,1900.10,'3-10-1990',2007,1004),
(3005,5160.45,'3-10-1990',2003,1002),
(3006,1098.16,'3-10-1990',2008,1007),
(3009 ,1713.23,'4-10-1990',2002,1003),
(3007,75.75,'4-10-1990',2004,1002),
(3008,4273.00,'5-10-1990',2006,1001),
(3010,1309.95,'6-10-1990',2004,1002),
(3011,9891.88,'6-10-1990',2006,1001);

show tables;

-- QUESTION 1

select count(Sname) from salespeople
where Sname like 'a%' or Sname like 'A%';

-- QUESTION 2

select o.snum,s.Sname,sum(amt)
from orders o
join salespeople s
on s.Snum=o.Snum
group by amt,snum,s.Sname
having o.amt>2000;


-- QUESTION 3

select count(Sname) from salespeople
where City='Newyork';

-- QUESTION 4

select * from salespeople
where City in ('London','Paris');

-- QUESTION 5

select o.snum,s.Sname ,odate,count(o.snum) as number_of_orders 
from orders o
join salespeople s
on s.snum=o.snum
group by o.snum, odate ,s.sname
order by o.snum,odate;





