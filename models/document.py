from peewee import CharField, TextField, IntegerField

from models.base import BaseModel

class Document(BaseModel):
    identifier = CharField()
    description = TextField()
    review = IntegerField(default=0)