
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import Integer
from sqlalchemy import String
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/sukru/Ada_Flow/Projet_Final_Harmonie_Culturelle/project_f_h_c/database/hrmcultdb.db'
db = SQLAlchemy(app)
db.init_app(app)

class Membres(db.ModeL):
    id = db.Column(db.Integer, primary_key=True)
    user_first_name = db.Column(db.String(33), unique=True, nullable=False)
    user_last_name = db.Column(db.String(33), unique=True, nullable=False)
    email = db.Column(db.String(133), unique=True, nullable=False)
    phone_number = db.Column(db.String(33), unique=True, nullable=False)
    adresse = db.Column(db.String(33), unique=True, nullable=False)
    zip_code = db.Column(db.String(33), unique=True, nullable=False)
    ville = db.Column(db.String(33), unique=True, nullable=False)
    canton = db.Column(db.String(33), unique=True, nullable=False)
    idt_file = db.Column(db.String(133), nullable=False, default='default.jpg')
    canton = db.Column(db.String(33), unique=True, nullable=False)
    Read_and_accept = db.Column(db.Boolean(True), nullable=False)
    password = db.Column(db.String(35), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self, user_first_name, user_last_name, email, phone_number, adresse, zip_code, ville, canton, date_created ):
        self.user_first_name = user_first_name
        self.user_last_name = user_last_name
        self.email = email
        self.phone_number = phone_number
        self.adresse = adresse
        self.zip_code = zip_code
        self.ville = canton
        self.canton = canton
        self.date_created = date_created
        



SQLALCHEMY_TRACK_MODIFICATIONS = False
app.config['SECRET_KEY'] = 'firstloginflask'
sql_uri = 'sqlite:///db.sqlite'
sql_engine = create_engine(sql_uri)
sql_meta = MetaData(sql_engine)

from project_f_h_c import routes
def routes(app):
    db.create_all()
    return routes
