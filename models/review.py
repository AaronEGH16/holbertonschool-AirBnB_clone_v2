#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, String
from os import getenv


class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = "reviews"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        place = Column(String(1024), nullable=False)
        user_id = Column(String(60), nullable=False)
        place = Column(String(60), ForeignKey("user.id"), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
