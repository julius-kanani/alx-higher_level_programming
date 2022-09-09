#!/usr/bin/python3
""" 1-filter_states module. This module lists all states from the database
hbtn_0e_0_usa with a name starting with N. """


import MySQLdb
from sys import argv


def filter_states():
    """ Lists all states with a name starting with N from the database
        hbtn_0e_0_usa. """

    db = MySQLdb.connect(
            host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")

    rows = cursor.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states()
