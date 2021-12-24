#!/usr/bin/python3
"""
lists all State objects that contain the
letter a from the database hbtn_0e_6_usa
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
Base = declarative_base()

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], rgv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for id, name in session.query(State.id, State.name).order_by(State.id):
        if 'a' in name:
            print("{}: {}".format(id, name))
    session.close()
