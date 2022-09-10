#!/usr/bin/python3
""" 5-filter_cities module. This module takes in the name of a state as an
    argument and lists all cities of that state, using the database
    hbtn_0e_4_usa. """


import MySQLdb
from sys import argv


def filter_states():
    """ Lists all cities of a given state from the database
        hbtn_0e_4_usa. """

    db = MySQLdb.connect(
            host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute(
            "SELECT c.name \
                FROM cities as c \
                    JOIN states as s \
                        ON c.state_id = s.id \
             WHERE s.name = %s \
             ORDER BY c.id ASC;", (argv[4],)
            )

    rows = cursor.fetchall()
    out = []
    for row in rows:
        out.append(row[0])

    print(', '.join(out))

    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states()
