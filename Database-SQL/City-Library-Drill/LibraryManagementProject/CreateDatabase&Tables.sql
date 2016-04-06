USE master
GO

CREATE DATABASE LibraryManagementSystem
GO

USE LibraryManagementSystem
GO

CREATE TABLE Book
(
BookID INT not null PRIMARY KEY,
Title varchar(50) not null,
PublisherName varchar(50)
)

CREATE TABLE Book_Authors
(
BookID INT not null PRIMARY KEY,
AuthorName varchar(50)
)

CREATE TABLE Book_Copies
(
BookID INT not null,
BranchID INT not null,
No_Of_Copies INT,
)

CREATE TABLE Book_Loans
(
BookID INT not null,
BranchID INT not null,
CardNo INT,
DateOut date,
DueDate date,
)

CREATE TABLE Publisher
(
Name varchar(50) PRIMARY KEY,
[Address] varchar(50),
Phone varchar(20),
)

CREATE TABLE Library_Branch
(
BranchID INT not null PRIMARY KEY,
BranchName varchar(50),
[Address] varchar(50)
)

CREATE TABLE Borrower
(
CardNo INT PRIMARY KEY,
Name Varchar(50),
[Address] varchar(50),
Phone varchar(20),
)

