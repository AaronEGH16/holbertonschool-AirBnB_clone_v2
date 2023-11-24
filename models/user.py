#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey,  String

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nulleable=False)
    password = Column(String(128), nulleable=False)
    first_name = Column(String(128), nulleable=False)
    last_name = Column(String(128), nulleable=False)
