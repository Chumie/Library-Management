create database Library

USE library;

CREATE TABLE Members (
    member_id INT NOT NULL,
    name VARCHAR(40) NOT NULL,
    PRIMARY KEY (member_id)
);

create table borrowed_books (
id int not null,
member_id int not null,
ISBN char(13) not null,
primary key (ISBN));

create table books (
book_id int not null,
title varchar(30),
author varchar(30),
isbn CHAR(13) not null,
primary key (ISBN)