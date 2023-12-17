#!/usr/bin/python3
"""
    A script that adds the State object
    “Louisiana” to the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
    new_state = State(name='Louisiana')

    app_session.add(new_state)
    app_session.commit()

    new_state_id = app_session.query(State).filter(
            State.name == "Louisiana").first()

    if new_state_id is not None:
        print(new_state_id.id)
    app_session.close()
