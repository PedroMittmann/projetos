from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__) # Instância 'app' é criada AQUI
app.config.from_object(Config)

db = SQLAlchemy(app) # Instância 'db' é criada AQUI, depende de 'app'

# IMPORTANTE: As rotas devem ser importadas DEPOIS que 'app' e 'db' são definidos
# Se você importar 'routes' antes, 'app' e 'db' podem não estar disponíveis quando 'routes.py' tentar usá-los.
import routes

if __name__ == '__main__':
    app.run(debug=True)