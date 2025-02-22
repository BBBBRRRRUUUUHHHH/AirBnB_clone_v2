#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import os
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    

    def __init__(self, *args, **kwargs):
        """
        Instatntiates a new model
        """
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """return to string representation"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Uuodate time"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance to dict"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                        (str(type(self)).split('.')[-1]).split('\'')[0]})
        if hasattr(self, 'created_at') and self.created_at:
            dictionary['created_at'] = self.created_at.isoformat()
    
        if hasattr(self, 'updated_at') and self.updated_at:
            dictionary['updated_at'] = self.updated_at.isoformat()

        if "_sa_instance_state" in dictionary.keys():
            del dictionary["_sa_instance_state"]
    
        return dictionary

    def delete(self):
        """ delete current instance """
        from models import storage
        storage.delete(self)
