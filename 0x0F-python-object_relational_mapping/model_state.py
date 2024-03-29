#!/usr/bin/python3
""" The model_state module. First state model.
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class State(Base):
    """ Defines the State Model

        Attributes:
            id (int): The class unique id, that is auto-generated.
            name (str): The name of the state.
    """
    __tablename__ = "states"

    id = Column(
            Integer, primary_key=True, unique=True, nullable=False,
            autoincrement=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        """ Returns a string representation instance of the State. """

        return "State(id={:d}, name={:s})".format(self.id, self.name)
