#!/usr/bin/python3
"""
    A script that lists all State objects
    from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    """
        Access to the database and get the states
        from the database.
    """
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    app_session = Session()

    for instance in app_session.query(State).order_by(State.id):
        print(f"{instance.id}: {instance.name}")
