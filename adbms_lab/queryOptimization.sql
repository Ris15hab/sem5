use world;

show tables;

select * from city;
optimize table city;

-- Nested Loop
select Name from city 
where Population > (select AVG(Population) from city) and
CountryCode in (select Code from country
where Population > (select AVG(Population) from country));
optimize table city,country;

select Name 
from city where CountryCode in (
select Code from country where Continent = 'Asia');
optimize table city,country;

select Name from country 
where Population > ( select avg(Population) from city where CountryCode = 'Ind');
optimize table city,country;

-- Right Join
select count(*) from city right join country 
on CountryCode in (select Code from country where LifeExpectancy > 80.0);
optimize table city,country;

-- Inner Join
select count(*) from city inner join country 
on CountryCode in (select Code from country where LifeExpectancy > 80.0);
optimize table city,country;

-- Index 
create index Name on country(Name);
select * from country where Name = 'India';