#!/usr/bin/python3
"""model state class"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Sequence, String


Base = declarative_base()


class State(Base):
    """state class"""
    __tablename__ = 'states'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
