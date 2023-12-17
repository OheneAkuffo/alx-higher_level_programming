#!/usr/bin/python3
"""
    A script that lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    connection = MySQLdb.connect(
            host="localhost", user=argv[1],
            passwd=argv[2], port=3306, db=argv[3])

    db_cursor = connection.cursor()

    db_cursor.execute(
        "SELECT * from states WHERE name LIKE BINARY 'N%' \
        ORDER BY states.id ASC")
    selected_row = db_cursor.fetchall()

    for row in selected_row:
        print(row)
