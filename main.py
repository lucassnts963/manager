from services.database import Database
from models.user import User
from models.budget import Budget
from models.product import Product, StockTransaction
from models.document import Document
from models.need import Need

db = Database()

db.create_tables([User, Budget, Product, Document, Need, StockTransaction])

#with db.connection():
    #new_user = Budget.create(description='Primeiro Orçamento')

db.close()