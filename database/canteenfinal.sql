-- Create database
CREATE DATABASE canteen_database2;
USE canteen_database2;

-- Customer Table
CREATE TABLE tbcustomer (
    customerid VARCHAR(50) PRIMARY KEY,
    name VARCHAR(255),
    phone VARCHAR(20),
    email VARCHAR(50),
    address VARCHAR(255),
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50)
);

-- Admin Table
CREATE TABLE tbadmin (
    username VARCHAR(50) UNIQUE PRIMARY KEY,
    password VARCHAR(50)
);

-- Staff Table
CREATE TABLE tbstaff (
    staffid VARCHAR(50) PRIMARY KEY,
    name VARCHAR(255),
    phone VARCHAR(20),
    email VARCHAR(50),
    address VARCHAR(50),
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50)
);

-- Feedback Table
CREATE TABLE tbfeedback (
    feedbackid VARCHAR(50) PRIMARY KEY,
    customerid VARCHAR(50),
    title VARCHAR(255),
    description TEXT,
    FOREIGN KEY (customerid) REFERENCES tbcustomer(customerid)
);
CREATE TABLE tbfoodcategory (
    categoryid VARCHAR(10) PRIMARY KEY ,
    name VARCHAR(255) NOT NULL
);
-- Food Items Table
CREATE TABLE tbfooditems (
    itemid VARCHAR(50) PRIMARY KEY,
    name VARCHAR(255),
    rate VARCHAR(10),
    categoryid VARCHAR(10),
    FOREIGN KEY (categoryid) REFERENCES tbfoodcategory(categoryid)
);

-- Order Table
CREATE TABLE tborder (
    orderid VARCHAR(50) PRIMARY KEY,
    customerid VARCHAR(50),
    itemid VARCHAR(50),
    quantity VARCHAR(10),
    billamount DECIMAL(10, 2),
    paymentstatus VARCHAR(20),
    status VARCHAR(20),
    FOREIGN KEY (customerid) REFERENCES tbcustomer(customerid),
    FOREIGN KEY (itemid) REFERENCES tbfooditems(itemid)
 
);

-- Chef Table
CREATE TABLE tbchef (
    chefid VARCHAR(50) PRIMARY KEY,
    name VARCHAR(255),
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50)
);


