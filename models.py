from app import db # Importa a instância 'db' do SQLAlchemy de app.py
from datetime import datetime

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False) # ALTERADO: name -> nome
    produtos = db.relationship('Produto', backref='categoria', lazy=True) # ALTERADO: products -> produtos

    def __repr__(self):
        return f"<Categoria '{self.nome}'>" # ALTERADO: self.name -> self.nome

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False) # ALTERADO: name -> nome
    descricao = db.Column(db.Text, nullable=True) # ALTERADO: description -> descricao
    preco = db.Column(db.Float, nullable=False) # ALTERADO: price -> preco
    quantidade_estoque = db.Column(db.Integer, nullable=False, default=0) # ALTERADO: stock_quantity -> quantidade_estoque
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    data_adicao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # ALTERADO: date_added -> data_adicao
    ultima_atualizacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow) # ALTERADO: last_updated -> ultima_atualizacao

    def __repr__(self):
        return f"<Produto '{self.nome}'>" # ALTERADO: self.name -> self.nome

class Usuario(db.Model): # Supondo que você quis usar 'Usuario' em vez de 'User' para manter a padronização
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False) # Decida se será 'nome_usuario' ou 'username'
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False) # Decida se será 'eh_admin'
    data_cadastro = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # ALTERADO: date_joined -> data_cadastro

    def __repr__(self):
        return f"<Usuario '{self.username}'>" # OU '{self.nome_usuario}' se mudar o campo