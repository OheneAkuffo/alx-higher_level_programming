#!/usr/bin/python3
"""
    A script 14-model_city_fetch_by_state.py that prints
    all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    """
        Access to the database and get the cities
        from the database.
    """

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    app_session = Session()
    states = app_session.query(City, State).join(State)

    for city, state in states.all():
        print("{}: ({}) {}".format(
            state.name, city.id, city.name))
