from peewee import CharField, TextField, FloatField, ForeignKeyField

from models.base import BaseModel
from models.document import Document

class Product(BaseModel):
    cod = CharField()
    description = TextField()
    category = CharField()
    unity = CharField()
    weight = FloatField()
    
class StockTransaction(BaseModel):
    class Meta:
        table_name = 'stock'
    product = ForeignKeyField(Product, backref='products')
    document = ForeignKeyField(Document, backref='documents')
    quantity = FloatField()
