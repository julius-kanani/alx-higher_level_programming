#!/usr/bin/python3
""" 8-model_state_fetch_first module. Lists the first State object. """

from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # initialize engine
    engine = engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                    .format(argv[1], argv[2], argv[3]),
                                    pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Initialize session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the hbtn_0e_6_usa
    state = session.query(State).first()

    # Print out the result set
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))

    # Close the connection
    session.close()
