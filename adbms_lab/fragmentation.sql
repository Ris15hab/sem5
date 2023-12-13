-- range
create table students(
    id int primary key,
    name varchar(50),
    phone varchar(50)
)partition by range(id)(
    partition p0 values less than (3),
    partition p1 values less than (4),
    partition p2 values less than (5),
    partition p3 values less than maxvalue,
);

insert into students values
(1,'rishab','8779723022'),
(2,'mahek','8291002606'),
(3,'rishab1','8779723023'),
(4,'rishab2','87797230224');

select * from students partition(p0);

-- list
create table students(
    id int primary key,
    name varchar(50),
    phone varchar(50)
)partition by list(id)(
    partition p0 values in (1,2),
    partition p1 values in (4),
    partition p2 values in (3),
);

insert into students values
(1,'rishab','8779723022'),
(2,'mahek','8291002606'),
(3,'rishab1','8779723023'),
(4,'rishab2','87797230224');

select * from students partition(p1);

-- hash
create table students(
    id int primary key,
    name varchar(50),
    phone varchar(50)
)partition by hash(id)(
    partition p0 
    partition p1 
    partition p2 
);

insert into students values
(1,'rishab','8779723022'),
(2,'mahek','8291002606'),
(3,'rishab1','8779723023'),
(4,'rishab2','87797230224');

select * from students partition(p0);

-- key
create table students(
    id int primary key,
    name varchar(50),
    phone varchar(50)
)partition by key(id) partitions 3;

insert into students values
(1,'rishab','8779723022'),
(2,'mahek','8291002606'),
(3,'rishab1','8779723023'),
(4,'rishab2','87797230224');

select * from students partition(p0);