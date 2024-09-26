from peewee import TextField, CharField, FloatField

from models.base import BaseModel

class Budget(BaseModel):
    name = CharField()
    description = TextField()
    amount = FloatField()