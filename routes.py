from flask import render_template, url_for, flash, redirect, request
from app import app, db # Importa a instância do Flask 'app' e o SQLAlchemy 'db'
from models import Categoria, Produto, Usuario # Importa seus modelos
from forms import FormularioCategoria, FormularioProduto # Importa seus formulários

# Rota da Página Inicial
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', title='Início')

# Rota para Adicionar Categoria
@app.route("/categorias/nova", methods=['GET', 'POST'])
def nova_categoria():
    form = FormularioCategoria()
    if form.validate_on_submit(): # Verifica se o formulário foi enviado e é válido
        categoria = Categoria(nome=form.nome.data)
        db.session.add(categoria)
        db.session.commit()
        flash('Categoria criada com sucesso!', 'success') # Mensagem de sucesso
        return redirect(url_for('home')) # Redireciona para a página inicial ou outra rota
    return render_template('categorias/criar_categoria.html', title='Nova Categoria', form=form)

# Rota para Adicionar Produto
@app.route("/produtos/novo", methods=['GET', 'POST'])
def novo_produto():
    form = FormularioProduto()
    if form.validate_on_submit(): # Verifica se o formulário foi enviado e é válido
        produto = Produto(
            nome=form.nome.data,
            descricao=form.descricao.data,
            preco=form.preco.data,
            quantidade_estoque=form.quantidade_estoque.data,
            categoria_id=form.categoria.data
        )
        db.session.add(produto)
        db.session.commit()
        flash('Produto criado com sucesso!', 'success')
        return redirect(url_for('home'))
    return render_template('produtos/criar_produto.html', title='Novo Produto', form=form)
# Rota para Listar Categorias
@app.route("/categorias")
def listar_categorias():
    categorias = Categoria.query.order_by(Categoria.nome).all() # Busca todas as categorias no BD, ordenadas por nome
    return render_template('categorias/listar_categorias.html', title='Categorias', categorias=categorias)

# Rota para Listar Produtos
@app.route("/produtos")
def listar_produtos():
    produtos = Produto.query.order_by(Produto.nome).all() # Busca todos os produtos no BD, ordenados por nome
    return render_template('produtos/listar_produtos.html', title='Produtos', produtos=produtos)