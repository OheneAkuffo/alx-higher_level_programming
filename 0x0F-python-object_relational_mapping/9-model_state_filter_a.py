#!/usr/bin/python3
"""
    A  script that lists all State objects that
    contain the letter a from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    """
        Access to the database and get a state
        from the database.
    """

    engine = create_engine(
            "mysql://{}:{}@localhost:3306/{}".format(
                argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    app_session = Session()

    states = app_session.query(State).filter(
            State.name.contains('a'))

    if states is not None:
        for state in states:
            print(f"{state.id}: {state.name}")
