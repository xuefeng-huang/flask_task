from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)

from send_later import views