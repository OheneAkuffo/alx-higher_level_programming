0x00-python-hello_world

This repository contains Python scripts and C code for various tasks related to the basics of Python programming.

Files

0-run: A shell script that runs a Python script. The Python file name is saved in the environment variable $PYFILE.

1-run_inline: A shell script that runs Python code. The Python code is saved in the environment variable $PYCODE.

2-print.py: A Python script that prints the string "Programming is like building a multilingual puzzle" followed by a new line.

3-print_number.py: A Python script that prints an integer stored in the variable number, followed by the string "Battery street", and a new line. The variable number should not be cast to a string.

4-print_float.py: A Python script that prints a float stored in the variable number with a precision of 2 digits, followed by a new line. The variable number should not be cast to a string.

5-print_string.py: A Python script that prints a string stored in the variable str three times, followed by the first 9 characters of the string, and a new line. No loops or conditional statements are allowed.

6-concat.py: A Python script that prints "Welcome to Holberton School!" using the variables str1 and str2, without using any loops or conditional statements. The program is exactly 5 lines long.

7-edges.py: A Python script that extracts substrings from the variable word and prints them. It prints the first 3 letters, the last 2 letters, and the value of word without the first and last letters, each followed by a new line. The program is exactly 8 lines long and does not use any loops or conditional statements.

8-concat_edges.py: A Python script that prints "object-oriented programming with Python" using only the variables str1 and str2. The program is exactly 5 lines long and does not use any loops, conditional statements, or string literals.

9-easter_egg.py: A Python script that prints "The Zen of Python, by Tim Peters" followed by the Zen of Python itself. The program is maximum 98 characters long.

10-check_cycle.c: A C function that checks if a singly linked list has a cycle in it. The function returns 0 if there is no cycle and 1 if there is a cycle. Only the allowed functions write, printf, putchar, puts, malloc, and free can be used.

Environment Variables

The scripts use the following environment variables:

$PYFILE: Stores the name of the Python file to be executed.

$PYCODE: Stores the Python code to be executed
