from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
from app import db # Importa a instância do db para validações no banco de dados
from models import Categoria, Produto # Importa seus modelos (verifique os nomes em português!)

class FormularioCategoria(FlaskForm):
    nome = StringField('Nome da Categoria',
                       validators=[DataRequired(), Length(min=2, max=100)],
                       render_kw={"placeholder": "Ex: Eletrônicos, Roupas"})
    submit = SubmitField('Adicionar Categoria')

    def validate_nome(self, nome):
        # Verifica se já existe uma categoria com este nome
        categoria = Categoria.query.filter_by(nome=nome.data).first()
        if categoria:
            raise ValidationError('Já existe uma categoria com este nome. Por favor, escolha um nome diferente.')

class FormularioProduto(FlaskForm):
    nome = StringField('Nome do Produto',
                       validators=[DataRequired(), Length(min=2, max=100)],
                       render_kw={"placeholder": "Ex: Smartphone XYZ"})
    descricao = TextAreaField('Descrição',
                              render_kw={"placeholder": "Detalhes sobre o produto..."})
    preco = FloatField('Preço',
                       validators=[DataRequired(), NumberRange(min=0.01)],
                       render_kw={"placeholder": "0.00"})
    quantidade_estoque = IntegerField('Quantidade em Estoque',
                                      validators=[DataRequired(), NumberRange(min=0)],
                                      render_kw={"placeholder": "0"})
    categoria = SelectField('Categoria',
                            coerce=int, # Converte o valor selecionado para inteiro (o ID da categoria)
                            validators=[DataRequired()])
    submit = SubmitField('Salvar Produto')

    def __init__(self, *args, **kwargs):
        super(FormularioProduto, self).__init__(*args, **kwargs)
        self.categoria.choices = [(c.id, c.nome) for c in Categoria.query.order_by(Categoria.nome).all()]

    def validate_nome(self, nome):
        # Verifica se já existe um produto com este nome
        produto = Produto.query.filter_by(nome=nome.data).first()
        if produto:
            raise ValidationError('Já existe um produto com este nome. Por favor, escolha um nome diferente.')