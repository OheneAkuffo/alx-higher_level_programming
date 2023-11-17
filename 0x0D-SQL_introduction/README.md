Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General

What’s a database
What’s a relational database
What does SQL stand for
What’s MySQL
How to create a database in MySQL
What does DDL and DML stand for
How to CREATE or ALTER a table
How to SELECT data from a table
How to INSERT, UPDATE, or DELETE data
What are subqueries
How to use MySQL functions
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet the above learning objectives. You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work. You are not allowed to publish any content of this project. Any form of plagiarism is strictly forbidden and will result in removal from the program.

Requirements
General

Allowed editors: vi, vim, emacs
All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
All your files should end with a new line
All your SQL queries should have a comment just before (i.e., syntax above)
All your files should start with a comment describing the task
All SQL keywords should be in uppercase (SELECT, WHERE…)
Usage
Comments for your SQL file:

-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;

Tasks
0. List databases (mandatory)
Write a script that lists all databases of your MySQL server.

1. Create a database (mandatory)
Write a script that creates the database hbtn_0c_0 in your MySQL server.

If the database hbtn_0c_0 already exists, your script should not fail.
You are not allowed to use the SELECT or SHOW statements.
2. Delete a database (mandatory)
Write a script that deletes the database hbtn_0c_0 in your MySQL server.

If the database hbtn_0c_0 doesn’t exist, your script should not fail.
You are not allowed to use the SELECT or SHOW statements.

3. List tables (mandatory)
Write a script that lists all the tables of a database in your MySQL server.

The database name will be passed as an argument of the mysql command (in the following example: mysql is the name of the database).


Certainly, here's the README.md with various formatting tags added:

markdown
Copy code
# Project Name

**0x0D. SQL - Introduction**

## Project Details

- **Technology Stack**: SQL, MySQL
- **Author**: Guillaume
- **Weight**: 1
- **Project Start Date**: October 17, 2023, 6:00 AM
- **Project End Date**: October 18, 2023, 6:00 AM
- **Checker Release Date**: October 17, 2023, 12:00 PM
- An auto-review will be launched at the deadline.

## Concepts

For this project, we expect you to look at these concepts:

- **Databases**
- **Databases**

## Resources

Read or watch the following resources:

- [What is Database & SQL?](resource_link)
- [A Basic MySQL Tutorial](resource_link)
- **Basic SQL statements: DDL and DML** (no need to read the chapter "Privileges")
- **Basic queries: SQL and RA**
- **SQL technique: functions**
- **SQL technique: subqueries**
- **What makes the big difference between a backtick and an apostrophe?**
- [**MySQL Cheat Sheet**](resource_link)
- [**MySQL 8.0 SQL Statement Syntax**](resource_link)
- [**Installing MySQL in Ubuntu 20.04**](resource_link)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

**General**
- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s MySQL
- How to create a database in MySQL
- What does DDL and DML stand for
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE, or DELETE data
- What are subqueries
- How to use MySQL functions

## Copyright - Plagiarism

You are tasked to come up with solutions for the tasks below yourself to meet the above learning objectives. You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work. You are not allowed to publish any content of this project. Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

**General**
- Allowed editors: **vi, vim, emacs**
- All your files will be executed on **Ubuntu 20.04 LTS** using **MySQL 8.0** (version 8.0.25)
- All your files should end with a **new line**
- All your SQL queries should have a comment just before (i.e., **syntax above**)
- All your files should start with a comment describing the task
- All SQL keywords should be in uppercase (**SELECT, WHERE…**)

## Usage

Comments for your SQL file:

```sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
Install MySQL 8.0 on Ubuntu 20.04 LTS

shell
Copy code
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
Connect to your MySQL server:

shell
Copy code
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
Use “container-on-demand” to run MySQL

shell
Copy code
In the container, credentials are root/root

Ask for container Ubuntu 20.04
Connect via SSH
OR connect via the Web terminal
In the container, you should start MySQL before playing with it:
$ service mysql start
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p
Database                                                                                   
information_schema                                                                         
mysql                                                                                        
performance_schema                                                                         
sys
$
Quiz questions:
Great! You've completed the quiz successfully! Keep going! (Show quiz)

Tasks
0. List databases (mandatory)
Write a script that lists all databases of your MySQL server.

shell
Copy code
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password:
Database                                                                                     
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys
guillaume@ubuntu:~/$
Repo:
GitHub repository: alx-higher_level_programming
Directory: 0x0D-SQL_introduction
File: 0-list_databases.sql

1. Create a database (mandatory)
Write a script that creates the database hbtn_0c_0 in your MySQL server.

If the database hbtn_0c_0 already exists, your script should not fail.
You are not allowed to use the SELECT or SHOW statements.

shell
Copy code
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password:
Database
information_schema
hbtn_0c_0
mysql
performance_schema
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$
Repo:
GitHub repository: alx-higher_level_programming
Directory: 0x0D-SQL_introduction
File: 1-create_database_if_missing.sql

2. Delete a database (mandatory)
Write a script that deletes the database hbtn_0c_0 in your MySQL server.

If the database hbtn_0c_0 doesn’t exist, your script should not fail.
You are not allowed to use the SELECT or SHOW statements.

shell
Copy code
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password:
Database                                                                                     
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys
guillaume@ubuntu:~/$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password:
Database
information_schema
mysql
performance_schema
sys
guillaume@ubuntu:~/$
Repo:
GitHub repository: alx-higher_level_programming
Directory: 0x0D-SQL_introduction
File: 2-remove_database.sql

3. List tables (mandatory)
Write a script that lists all the tables of a database in your MySQL server.

The database name will be passed as an argument of the mysql command (in the following example: mysql is the name of the database).

4. First table (mandatory)
Write a script that creates a table called first_table in the current database in your MySQL server.

first_table description:

id INT

name VARCHAR(256)
The database name will be passed as an argument of the mysql command.
If the table first_table already exists, your script should not fail.
You are not allowed to use the SELECT or SHOW statements.

5. Full description (mandatory)
Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.

The database name will be passed as an argument of the mysql command.
You are not allowed to use the DESCRIBE or EXPLAIN statements.
8. Count 89 (mandatory)
Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

The database name will be passed as an argument of the mysql command.

9. Full creation (mandatory)
Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

second_table description:

id INT
name VARCHAR(256)
score INT
The database name will be passed as an argument to the mysql command.
If the table second_table already exists, your script should not fail.
You are not allowed to use the SELECT and SHOW statements.
Your script should create these records:

id = 1, name = “John”, score = 10
id = 2, name = “Alex”, score = 3
id = 3, name = “Bob”, score = 14
id = 4, name = “George”, score = 8
shell
Copy code
guillaume@ubuntu:~/$ cat 9-full_creation.sql | mysql -hlocalhost -

