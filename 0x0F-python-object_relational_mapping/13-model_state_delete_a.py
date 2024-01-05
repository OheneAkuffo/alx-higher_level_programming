#!/usr/bin/python3
"""
    A script that deletes all State objects
    with a name containing the letter a from the database
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    """
        Deletes State objects on the database.
    """
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    app_session = Session()

    states_to_delete = app_session.query(State).filter(
            State.name.contains('a'))

    if states_to_delete is not None:
        for state in states_to_delete:
            app_session.delete(state)

    app_session.commit()
    app_session.close()
