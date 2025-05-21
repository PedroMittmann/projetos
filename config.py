import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uma-chave-secreta-muito-dificil-de-adivinhar' # Use uma chave forte em produção!
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://app_user:Ab123456@localhost:5432/mittsoft'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Define para False para economizar memória