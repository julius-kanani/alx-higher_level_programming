#!/usr/bin/python3
""" 0-select_states module. This module lists all states from the database
hbtn_0e_0_usa. """


import MySQLdb
from sys import argv


def list_states():
    """ Lists all states from the database hbtn_0e_0_usa. """

    db = MySQLdb.connect(
            host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute(
            "SELECT c.id, c.name, s.name \
                FROM cities AS c \
                    JOIN states as s \
                        ON c.state_id = s.id \
             ORDER BY c.id ASC;"
            )

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states()
