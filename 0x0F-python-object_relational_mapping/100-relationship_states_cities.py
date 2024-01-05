#!/usr/bin/python3
"""
    A  script that creates the State “California”
    with the City “San Francisco” from the database
    hbtn_0e_100_usa: (100-relationship_states_cities.py)
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv
from urllib.parse import quote

if __name__ == "__main__":
    """
        Access to the database and get the cities
        from the database.
    """
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                argv[1], quote(argv[2]), argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    app_session = Session()

    state = State()
    city = City()

    state.name = 'California'
    city.name = 'San Francisco'

    state.cities.append(city)

    app_session.add(state)
    app_session.commit()
    app_session.close()
