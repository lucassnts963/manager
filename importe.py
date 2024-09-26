import csv, os

from peewee import fn

from services.database import Database
from services.database import Database
from models.product import Product
from models.document import Document
from models.need import Need

def process_csv_product(csv_path):

    db = Database()

    try:
        with open(csv_path, mode='r') as file:
            csv_reader = csv.DictReader(file, delimiter=';')
            with db.connection():
                for row in csv_reader:
                    cod = row['Código']
                    description = row['Descrição']
                    category = row['Categorias']
                    unity = row['Unidade']
                    weight = row['Peso']

                    # Função para processar o peso
                    weight = process_weight(weight)

                    if cod:
                        Product.create(
                            cod=cod, 
                            description=description, 
                            category=category, 
                            unity=unity, 
                            weight=weight
                        )
    except Exception as e:
        print(f"Erro ao processar CSV: {e}")

def process_weight(weight_str):
    """Processa o peso, convertendo a string com vírgula para float ou retornando None se estiver vazio."""
    if weight_str.strip() == '':
        return 0
    else:
        try:
            return float(weight_str.replace(',', '.'))
        except ValueError:
            print(f"Erro ao converter peso: {weight_str}")
            return None

def process_csv_documents(csv_path):
    from services.database import Database
    from models.document import Document
    
    db = Database()
    
    try:
        with open(csv_path, mode='r') as file:
            csv_reader = csv.DictReader(file, delimiter=';')
            with db.connection():
                for row in csv_reader:
                    identifier=row['Desenho']
                    description='{0} - {1}'.format(row['Descrição'], row['Tag'])
                    review=int(row['Rev. Isométrico'])
                    
                    if not identifier:
                        continue
                    
                    Document.create(
                        identifier=identifier,
                        description=description,
                        review=review
                        )
    except Exception as e:
        print(f'Erro ao processar CSV: {e}')

def process_csv_needs(csv_path):
    db = Database()
    
    try:
        with open(csv_path, mode='r') as file:
            csv_reader = csv.DictReader(file, delimiter=';')
            with db.connection():
                for row in csv_reader:
                    cod = row['Cód']
                    identifier = row['Desenho']
                    aplication = row['Aplicação']
                    quantity = row['Qtd. Desenho']

                    # Verificar se o produto existe pelo cod
                    try:
                        product = Product.get(Product.cod == cod)
                    except Product.DoesNotExist:
                        print(f"Produto com cod {cod} não encontrado.")
                        continue

                    # Verificar o documento pelo identifier e pegar o de maior revisão
                    document = (
                        Document
                        .select()
                        .where(Document.identifier == identifier)
                        .order_by(Document.review.desc())  # Seleciona o de maior revisão
                        .first()
                    )

                    if not document:
                        print(f"Documento com identifier {identifier} não encontrado.")
                        continue

                    # Criar a necessidade (need)
                    Need.create(
                        document_id=document.id,
                        product_id=product.id,
                        quantity=float(quantity.replace(',', '.')) if quantity.strip() else 0,
                        aplication=aplication
                    )
                    print(f"Necessidade criada para o produto {cod} e documento {identifier}.")

    except Exception as e:
        print(f"Erro ao processar CSV: {e}")


path = os.path.join('csv', 'necessidades.csv')

process_csv_needs(path)