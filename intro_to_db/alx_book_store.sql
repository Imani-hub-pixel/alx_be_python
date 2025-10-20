CREATE DATABASE alx_book_store;
USE alx_book_store;
CREATE TABLE Books(
    book_id  INT PRIMARY KEY,
    title VARCHAR(130),
    author_id INT,
    price DOUBLE,
    publication_date DATE,
     FOREIGN KEY(author_id) REFERENCES Authors(author_id)

);
CREATE TABLE Authors(
    author_id INT PRIMARY KEY,
    author_name VARCHAR(215)
);
CREATE TABLE Customers(
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT

);
CREATE TABLE orders(
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY(custormer_id) REFERENCES Customers(customer_id)
);
CREATE TABLE Order_Details(
    orderdetilid INT PRIMARY KEY,
    order_id INT,
    book_id INT,
    quantity DOUBLE,
    FOREIGN KEY(order_id) REFERENCES orders(order_id),
	FOREIGN KEY(book_id) REFERENCES Books(book_id)
    
);