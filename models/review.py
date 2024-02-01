#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import sqlalchemy


class Review(BaseModel, Base):
    """ Review classto store review information """
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = "reviews"
        place_id = Column(
            String(60),
            ForeignKey(
                'places.id',
                ondelete='CASCADE'),
            nullable=False)
        user_id = Column(
            String(60),
            ForeignKey(
                'users.id',
                ondelete='CASCADE'),
            nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
