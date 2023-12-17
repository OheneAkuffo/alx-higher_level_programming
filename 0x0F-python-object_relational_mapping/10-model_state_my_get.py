#!/usr/bin/python3
"""
    A script that prints the State object with the
    name passed as argument from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    """
        Access to the database and get a state
        from the database.
    """
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)

    app_session = Session()

    state = app_session.query(State).filter(State.name == argv[4]).first()

    if state is not None:
        print(state.id)
    else:
        print("Not found")
