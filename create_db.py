from app import app, db
from models import Categoria, Produto, Usuario # Importe seus modelos

with app.app_context():
    db.create_all()
    print("Tabelas do banco de dados criadas com sucesso!")