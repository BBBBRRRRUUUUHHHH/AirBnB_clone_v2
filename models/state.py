#!/usr/bin/python3
""" module of state """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from models.city import City
import models

storage_type = getenv("HBNB_TYPE_STORAGE")

class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')
    else:
        name = ""


        @property
        def cities(self):
            """cities method"""
            from models import storage
            from models.city import City

            cities_list = []
            citiesAll = storage.all(City)
            for city in citiesAll.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list

class State(BaseModel, Base):
    """ class of state"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')

    @property
    def cities(self):
        """cities list """
        records = models.storage.all()
        res = []
        for city in records.values():
            if self.id == city.state_id:
                res.append(city)
        return res
