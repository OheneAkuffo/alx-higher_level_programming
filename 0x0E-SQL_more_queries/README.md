SQL Queries and Tasks
This repository contains a set of SQL queries and tasks to be executed in a MySQL environment. The following tasks cover a range of database operations, including creating users, managing privileges, and querying data from databases.

Prerequisites
Before executing these tasks, make sure you have the following set up:

MySQL Server installed and running.
Appropriate permissions to create users and databases.
Task 0: My Privileges
Script: 0-privileges.sql

This script lists all privileges of the MySQL users user_0d_1 and user_0d_2 on the local server. If the users do not exist, it creates them with the necessary privileges.

Task 1: Root User
Script: 1-create_user.sql

This script creates a MySQL server user named user_0d_1 with all privileges and sets the password to user_0d_1_pwd. If the user already exists, it does not fail.

Task 2: Read User
Script: 2-create_read_user.sql

This script creates a database named hbtn_0d_2 and a user named user_0d_2 with only the SELECT privilege on the database. The password is set to user_0d_2_pwd. If the database or user already exists, it does not fail.

Task 3: Always a Name
Script: 3-force_name.sql

This script creates a table named force_name in the hbtn_0d_2 database with two columns: id (INT) and name (VARCHAR(256)) with a NOT NULL constraint on the name column.

Task 4: ID Can't Be Null
Script: 4-never_empty.sql

This script creates a table named id_not_null in the hbtn_0d_2 database with two columns: id (INT with default value 1) and name (VARCHAR(256)).

Task 5: Unique ID
Script: 5-unique_id.sql

This script creates a table named unique_id in the hbtn_0d_2 database with two columns: id (INT with default value 1 and unique constraint) and name (VARCHAR(256)).

Task 6: States Table
Script: 6-states.sql

This script creates a database named hbtn_0d_usa and a table named states with two columns: id (INT, unique, and primary key) and name (VARCHAR(256)).

Task 7: Cities Table
Script: 7-cities.sql

This script creates a table named cities in the hbtn_0d_usa database with three columns: id (INT, unique, and primary key), state_id (INT, foreign key referencing states.id), and name (VARCHAR(256)).
