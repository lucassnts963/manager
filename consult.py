from peewee import fn
from models.document import Document
from models.need import Need
from models.product import Product

def fetch_document_with_products(identifier):
    # Consulta para buscar o documento, sua descrição e os produtos associados com quantidade e descrição
    query = (Document
             .select(Document, Product, Need)
             .join(Need, on=(Document.id == Need.document_id))
             .join(Product, on=(Need.product_id == Product.id))
             .where(Document.identifier == identifier)
             )

    # Construir a string com os resultados
    result_str = ""
    
    for doc in query:
        if not result_str:
            # Monta a string com o identifier e descrição do documento
            result_str += f"Document: {doc.identifier} - {doc.description}\n"
            result_str += "Products:\n"
        
        # Adiciona cada produto com sua quantidade e descrição
        result_str += f"- Product: {doc.need.product.cod}, Description: {doc.need.product.description}, Quantity: {doc.need.quantity}\n"

    return result_str or f"No products found for document with identifier: {identifier}"
    
print(fetch_document_with_products('D3-2900-14-T-3028'))