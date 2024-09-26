from flask import Flask, render_template, request, jsonify, redirect

from peewee import fn

from models.document import Document
from models.need import Need
from models.budget import Budget
from models.product import Product, StockTransaction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/document/<identifier>')
def document(identifier):
    # Consultar o documento e suas necessidades associadas
    doc = Document.get_or_none(Document.identifier == identifier)
    if doc:
        needs = (Need
                 .select(Need, Need.product)
                 .where(Need.document == doc))
        return render_template('document.html', document=doc, needs=needs)
    else:
        return f"Documento com identificador {identifier} não encontrado.", 404

@app.route('/budgets')
def budgets():
    # Lógica para consultar os orçamentos
    budgets = Budget.select()
    return render_template('budgets.html', budgets=budgets)

@app.route('/add_budget', methods=['POST'])
def add_budget():
    name = request.form['name']
    amount = request.form['amount']
    description = request.form['description']

    # Cria o orçamento
    Budget.create(name=name, amount=amount, description=description)
    return redirect('/budgets')

@app.route('/update_budget/<int:id>', methods=['POST'])
def update_budget(id):
    data = request.json
    field = data['field']
    amount = data['amount']

    # Atualiza o orçamento
    budget = Budget.get_by_id(id)
    setattr(budget, field, amount)
    budget.save()
    return jsonify(success=True)

@app.route('/delete_budget/<int:id>', methods=['DELETE'])
def delete_budget(id):
    budget = Budget.get_by_id(id)
    budget.delete_instance()
    return jsonify(success=True)

@app.route('/products')
def products():
    products = Product.select()
    return render_template('products.html', products=products)
    
@app.route('/stock')
def stock():
    products = (Product.select(Product, fn.SUM(StockTransaction.quantity).alias('stock'))
    .join(StockTransaction, on=(Product.id == StockTransaction.product_id)).group_by(Product))
    return render_template('stock.html', products=products)

@app.route('/documents')
def documents():
    # Lógica para consultar os documentos
    return render_template('documents.html')

@app.route('/needs')
def needs():
    # Lógica para consultar e alterar as necessidades
    return render_template('needs.html')

if __name__ == '__main__':
    app.run(debug=True)