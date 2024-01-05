#!/usr/bin/python3

"""
    A script that takes in arguments and displays all
    values in the states table of hbtn_0e_0_usa where
    name matches the argument.
    But this time, the is safe from MySQL injections
"""

from sys import argv
import MySQLdb as db

if __name__ == "__main__":
    connection = db.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    query = "SELECT * FROM states WHERE name LIKE \
            BINARY %(search_name)s ORDER BY states.id ASC"

    cursor.execute(query, {'search_name': argv[4]})

    selected_rows = cursor.fetchall()

    for row in selected_rows:
        print(row)
