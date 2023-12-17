#!/usr/bin/python3
"""
    A script that lists all cities from
    the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb as db

if __name__ == "__main__":
    connection = db.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    query = "SELECT cities.id, cities.name, states.name \
            FROM cities INNER JOIN states \
            ON cities.state_id = states.id \
            ORDER BY cities.id ASC"

    cursor.execute(query)
    selected_cities = cursor.fetchall()

    for row in selected_cities:
        print(row)
