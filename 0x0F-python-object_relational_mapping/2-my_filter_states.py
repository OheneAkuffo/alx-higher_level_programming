#!/usr/bin/python3
"""
    A script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument
"""

from sys import argv
import MySQLdb as db

if __name__ == "__main__":
    search_name = argv[4]
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
            ORDER BY states.id".format(search_name)
    connection = db.connect(
                host="localhost", port=3306, user=argv[1],
                passwd=argv[2], db=argv[3])
    db_cursor = connection.cursor()

    db_cursor.execute(query)

    selected_row = db_cursor.fetchall()

    for row in selected_row:
        print(row)
