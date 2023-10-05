#!/usr/bin/python3
""" city module """
import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class City(BaseModel, Base):
<<<<<<< HEAD
        """ The city class, contains state ID and name """
        __tablename__ = 'cities'
        if storage_type == "db":
            name = Column(String(128), nullable=False)
            state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
            places = relationship('Place', backref='cities')
        else:
            name = ""
            state_id = ""
=======
    """city class"""
    __tablename__ = 'cities'
    state_id = Column(
        String(60), ForeignKey('states.id'), nullable=False
        ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    name = Column(
        String(128), nullable=False
        ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    places = relationship(
        'Place', cascade='all, delete, delete-orphan', backref='cities'
        ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
>>>>>>> ee6bc2a7072293464cf3777b828863e8745d746c
