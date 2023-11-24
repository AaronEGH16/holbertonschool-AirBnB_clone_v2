#!/usr/bin/python3
""""""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """"""
    __engine = None
    __session = None

    def __init__(self):
        """"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV", "none")

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                user, pwd, host, database),
            pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """"""
        obj_cls = {"User": User, "BaseModel": BaseModel,
                   "State": State,
                   "City": City}
        db_dict = {}

        if cls is not None and cls != "":
            query = (self.__session).query(obj_cls[cls]).all()
            for objects in query:
                key = f"{objects.__class__.__name__}.{objects.id}"
                db_dict[key] = objects
        else:
            for cls_name, cls_type in obj_cls.items():
                if cls_name != "BaseModel":
                    query = (self.__session).query(cls_type).all()
                    for objects in query:
                        key = f"{objects.__class__.__name__}.{objects.id}"
                        db_dict[key] = objects
        return db_dict

    def new(self, obj):
        """"""
        (self.__session).add(obj)

    def save(self):
        """"""
        (self.__session).commit()

    def delete(self, obj=None):
        """"""
        if obj is not None:
            (self.__session).delete(obj)

    def reload(self):
        """"""
        self.__session = Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False)
            )
        self.__session = Session()
