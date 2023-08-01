#!/usr/bin/python3
"""model state class"""
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
import sys

if __name__ == "__main__":
    u = sys.argv[1]
    p = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(u, p, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    result = session.query(City, State).filter(City.state_id == State.id).all()
    for cities, states in result:
        print(f"{states.name}: ({cities.id}) {cities.name}")
    session.commit()
    session.close()
