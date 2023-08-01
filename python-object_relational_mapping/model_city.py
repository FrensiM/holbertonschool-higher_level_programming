#!/usr/bin/python3
"""model state class"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy import ForeignKey


Base = declarative_base()


class City(Base):
    """state class"""
    __tablename__ = 'cities'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
