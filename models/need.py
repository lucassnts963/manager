from peewee import ForeignKeyField, IntegerField, CharField

from models.base import BaseModel
from models.document import Document
from models.product import Product

class Need(BaseModel):
    document = ForeignKeyField(Document, backref='documents')
    product = ForeignKeyField(Product, backref='products')
    quantity = IntegerField()
    aplication = CharField()
    page = IntegerField()
    item = IntegerField()