#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey,  String
from os import getenv


class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = "reviews"
    if getenv("HBNB_TYPE_STORAGE", "fs") == "db":
        place = Column(string(1024), nullable=False)
        user_id = Column(string(60), nullable=False)
        place = Column(string(60), nullable=False, ForeignKey("user.id"))
    else:
        place_id = ""
        user_id = ""
        text = ""
