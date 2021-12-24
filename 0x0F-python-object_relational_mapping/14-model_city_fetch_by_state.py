#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for st, ct in session.query(State, City).\
            order_by(City.id).\
            filter(City.state_id == State.id).\
            all():
        print("{}: ({}) {}".format(st.name, ct.id, ct.name))
    session.close()
