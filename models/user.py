from peewee import CharField

from models.base import BaseModel

class User(BaseModel):
    username = CharField(unique=True)