import os

SECRET_KEY = 'you-will-never-guess'
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'email.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True