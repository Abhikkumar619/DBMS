CREATE TABLE MANAGER(
ManagerID NUMBER(10) PRIMARY KEY,
FName VARCHAR(20) NOT NULL,
LName VARCHAR(15) NOT NULL
);

INSERT INTO MANAGER (ManagerID ,FName, LName) VALUES (001, 'Abishek', 'yadav');
INSERT INTO MANAGER ( ManagerID, FName, LName) VALUES( 002, 'Laddu', 'kumar');
SELECT * FROM MANAGER;


CREATE TABLE CUSTOMER
(
CustomerID NUMBER(10) PRIMARY KEY,
FName VARCHAR(20),
LName VARCHAR(15)
);
desc MANAGER;
INSERT INTO CUSTOMER (CustomerID, FName, LName) VALUES (101, 'Rishav', 'sah');
INSERT INTO CUSTOMER (CustomerID, FName, LName) VALUES (102, 'Nabin', 'Purbey');
SELECT * FROM CUSTOMER;



CREATE TABLE STORE(
StoreID NUMBER(10) PRIMARY KEY,
City_addrs VARCHAR(20) NOT NULL,
Street_addrs VARCHAR(15) NOT NULL,
Postcode NUMBER(8) NOT NULL,
ManagerID NUMBER(10)NOT NULL REFERENCES MANAGER(ManagerID),
JoinDate DATE NOT  NULL
);
ALTER TABLE STORE MODIFY JoinDate NULL;
DESC STORE;
INSERT INTO STORE (StoreID, City_addrs, Street_addrs, Postcode, managerID, JoinDate) VALUES (111, 'chndigard ', 'vavar', 747, 001, to_date('2001-1-2','yyyy-mm-dd');


CREATE TABLE CUSTOMER
(
CustomerID NUMBER(10) PRIMARY KEY,
FName VARCHAR(20),
LName VARCHAR(15)
);

DESC CUSTOMER;
INSERT INTO CUSTOMER( customerID, FName, LName) VALUES(201, 'subasah', 'yadav');
INSERT INTO CUSTOMER( customerID, FName, LName) VALUES(202, 'bhanu', 'sah');

CREATE TABLE ORDERS
(
OrderID NUMBER(10) PRIMARY KEY,
Order_Date DATE NOT NULL,
Order_Time TIMESTAMP NOT NULL,
OCompleted_Date DATE NOT NULL,
OCompleted_Time TIMESTAMP NOT NULL,
CustomerID NUMBER(10) REFERENCES CUSTOMER(CustomerID),
StoreID NUMBER(10) REFERENCES STORE(StoreID),
BreadID NUMBER(10) REFERENCES BREAD(BreadID),
TotalCost NUMBER(8,2) NOT NULL
);
desc orders;

INSERT INTO ORDERS ( OrderID, Order_Date, Order_Time, OCompleted_Date, OCompleted_Time, CustomerID, StoreID, BreadID, TotalCost) VALUES
( 401, to_date('2001-1-1','yyyy-mm-dd'), to_timestamp('2001-01-01 10:12:12','YYYY-MM-DD HH:MI:SS'), to_date('2001-1-2','yyyy-mm-dd'), to_timestamp('2001-01-02 11:13:12','YYYY-MM-DD HH:MI:SS') , 201, 111, 301, 3233.12);
 
select * from orders; 
CREATE TABLE BREAD
(
BreadID NUMBER PRIMARY KEY,
BreadName VARCHAR(15) UNIQUE,s
Calories NUMBER(4,2) NOT NULL,
Price NUMBER(8,2) NOT NULL
);
INSERT INTO BREAD (BreadID, BreadName, Calories, Price) VALUES (301, 'Brown', 10.2, 25);
INSERT INTO BREAD (BreadID, BreadName, Calories, Price) VALUES (302, 'Herbs', 12.6, 30);
INSERT INTO BREAD (BreadID, BreadName, Calories, Price) VALUES (303, 'Cheese', 20.8, 50);

SELECT * FROM BREAD;



CREATE TABLE SANDWISHMENU
(
SandwishID NUMBER(10) PRIMARY KEY,
SandwishName VARCHAR(15) UNIQUE
);

DESC SANDWISHMENU;
INSERT INTO SANDWISHMENU (SandwishID, SandwishName) VALUES (601, 'Tuna haven');
SELECT * FROM SANDWISHMENU;

CREATE TABLE CATEGORY 
(
CategoryID NUMBER(10) PRIMARY KEY,
CategoryNAME VARCHAR(15) UNIQUE
);
DESC CATEGORY;
INSERT INTO CATEGORY ( CategoryID, CategoryNAME) VALUES ( 701, 'Vegetable');
INSERT INTO CATEGORY ( CategoryID, CategoryNAME) VALUES ( 702, 'Pouletry');
SELECT * FROM CATEGORY;


CREATE TABLE FILLING
(
FillingID NUMBER(10) PRIMARY KEY, 
FllingName VARCHAR(15) UNIQUE,
Calories_pgram NUMBER(4,2) NOT NULL,
Price_pgram NUMBER(8,2) NOT NULL,
CatogryID NUMBER(10) REFERENCES CATEGORY(CategoryID)
);

DESC FILLING;
INSERT INTO FILLING( FillingID, FllingName, Calories_pgram, Price_pgram, CatogryID) VALUES ( 801, 'Tomato', 20.5, 0.5, 701);
INSERT INTO FILLING( FillingID, FllingName, Calories_pgram, Price_pgram, CatogryID) VALUES ( 802, 'rost', 25.5, 1.5, 702);
SELECT * FROM FILLING;


CREATE TABLE INGERIDENT
(
SandwishID NUMBER(10) REFERENCES SANDWISHMENU(SandwishID),
FillingID NUMBER(10) REFERENCES FILLING(FillingID),
Totalquentity NUMBER(5) NOT NULL
);
INSERT INTO INGERIDENT (SandwishID , FillingID, Totalquentity) VALUES(601, 801, 10);
INSERT INTO INGERIDENT (SandwishID , FillingID, Totalquentity) VALUES(601, 802, 10);
SELECT * FROM INGERIDENT;

DESC INGERIDENT;
SELECT * FROM Sandwishmenu;
