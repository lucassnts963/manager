from peewee import PostgresqlDatabase
from contextlib import contextmanager

class Database:
    def __init__(self):
        # Inicializa o banco de dados com o nome fornecido
        self.db = PostgresqlDatabase('montisol', user='lucas', password='123456', host='localhost', port=5432)

    def connect(self):
        """Conecta ao banco de dados."""
        if self.db.is_closed():
            print("Conectando ao banco de dados...")
            self.db.connect()

    def close(self):
        """Fecha a conexão com o banco de dados."""
        if not self.db.is_closed():
            print("Fechando conexão com o banco de dados...")
            self.db.close()

    @contextmanager
    def connection(self):
        """Gerencia a conexão ao banco de dados com contexto."""
        self.connect()
        try:
            yield
        finally:
            self.close()

    def create_tables(self, models):
        """Cria tabelas a partir de uma lista de modelos."""
        with self.connection():
            self.db.create_tables(models)
            print("Tabelas criadas com sucesso!")

    def drop_tables(self, models):
        """Remove tabelas a partir de uma lista de modelos."""
        with self.connection():
            self.db.drop_tables(models)
            print("Tabelas removidas com sucesso!")