#!/usr/bin/python3
""" The model_city module. Cities in state model.
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base, State


class City(Base):
    """ Defines the City Model

        Attributes:
            id (int): The class unique id, that is auto-generated.
            name (str): The name of the city.
    """
    __tablename__ = "cities"

    id = Column(
            Integer, primary_key=True, unique=True, nullable=False,
            autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __repr__(self):
        """ Returns a string representation instance of the city. """

        return "City(id={:d}, name={:s} state_id={:d})".format(
                self.id, self.name, self.state_id)
