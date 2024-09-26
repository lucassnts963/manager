from peewee import Model
from services.database import Database

database = Database()

class BaseModel(Model):
    class Meta:
        database = database.db