#!/usr/bin/python3
""" 7-model_state_fetch_all module. Lists all State objects from the
    hbtn_0e_6_usa database. """

from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def model_state_fetch_all(username=argv[1], passwd=argv[2], db=argv[3]):
    """ Lists all State objects from the database hbtn_0e_6_usa. """

    # initialize engine
    engine = engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(username, passwd, db),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Initialize session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the hbtn_0e_6_usa
    query = session.query(State).order_by(State.id).all()

    # Print out the result set
    for record in query:
        print("{}: {}".format(record.id, record.name))

    # Close the connection
    session.close()


if __name__ == "__main__":
    model_state_fetch_all()
