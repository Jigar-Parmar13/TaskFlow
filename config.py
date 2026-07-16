import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Flask application configuration class."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'taskflow-dev-secret-key-9a8b7c6d5e'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'sqlite:///{os.path.join(BASE_DIR, "taskflow.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
