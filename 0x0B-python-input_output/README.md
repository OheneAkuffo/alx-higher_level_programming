#Python - Input/Output#

This project focuses on working with input/output operations in Python. It covers various tasks related to file handling, serialization, and deserialization using JSON.

Learning Objectives By completing this project, you will gain a better understanding of the following concepts:

Opening and reading files in Python

Writing text to a file

Reading file content

Moving the cursor within a file

Ensuring file closure after use using the with statement

Working with JSON (JavaScript Object Notation)

Serialization and deserialization of Python data structures

Converting Python objects to JSON strings

Converting JSON strings to Python objects

Requirements Python 3.8.5 pycodestyle 2.8.*

All Python scripts must be executable and start with #!/usr/bin/python3

All test files should have the extension .txt

Test cases should be executed using the command python3 -m doctest ./tests/*

All modules, classes, and functions should have proper documentation

Project Tasks

The project consists of the following tasks:

Read file
Write to a file
Append to a file
To JSON string
From JSON string to Object
Save Object to a file
Create object from a JSON file
Each task has its own Python script and a corresponding test file in the tests folder.
Usage To run a specific task, you can execute the corresponding Python script from the command line. For example:

$ ./0-read_file.py To run the test cases for a task, you can use the following command:

$ python3 -m doctest ./tests/FILE_NAME.txt
Make sure to replace FILE_NAME with the appropriate test file name.
File Descriptions 0-read_file.py: Script to read and print the contents of a text file.

1-write_file.py: Script to write a string to a text file and return the number of characters written.

2-append_write.py: Script to append a string to the end of a text file and return the number of characters added.

3-to_json_string.py: Script to convert a Python object (string) to a JSON string representation

4-from_json_string.py: Script to convert a JSON string to a Python object.

5-save_to_json_file.py: Script to save a Python object to a text file in JSON format.

6-load_from_json_file.py: Script to load a Python object from a JSON file.

Testing The project includes test files for each task in the tests folder. You can run the test cases using the following command:

$ python3 -m doctest ./tests/FILE_NAME.txt
