#!/usr/bin/python3

"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
        Establish database connections.
        Make send a query to the database and print output
    """
    connection = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states")
    selected_rows = cursor.fetchall()

    for row in selected_rows:
        print(row)
