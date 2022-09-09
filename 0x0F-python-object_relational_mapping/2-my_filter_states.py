#!/usr/bin/python3
""" 2-my_filter_states module. This module filters all states from the
database hbtn_0e_0_usa using user input. """


import MySQLdb
from sys import argv


def filter_states():
    """ Filters all states with a name that matches the user input from
        the database hbtn_0e_0_usa. """

    db = MySQLdb.connect(
            host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id \
                    ASC;".format(argv[4]))

    rows = cursor.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states()
