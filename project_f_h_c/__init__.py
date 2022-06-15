from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

SQLALCHEMY_TRACK_MODIFICATIONS = True

app.config['SECRET_KEY'] = 'firstloginflask'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hrmcultdb.db'

db = SQLAlchemy(app)

db.create_all()


from project_f_h_c import routes

def routes(app):
    return routes