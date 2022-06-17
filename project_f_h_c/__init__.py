from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'firstloginflask'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/sukru/Ada_Flow/Projet_Final_Harmonie_Culturelle/project_f_h_c/database/db.sqlite'
app.config['SQLALCHEMY_ECHO'] = True        
db = SQLAlchemy(app)

from project_f_h_c import routes
def routes(app):
    return routes



# 2tables créer

# sql_membres = Table('membreTable', sql_meta, Column('membre_id',Integer, primary_key=True), Column ('user_first_name', String), 
# Column ('user_last_name', String), Column ('email', String), Column ('phone_number', String), Column ('adresse', String), 
# Column ('zip_code', Integer), Column ('ville', String), Column ('canton', String), Column ('idt_file', String), Column 
# ('Read_and_accept', String), Column ('password', String), Column ('date_created', String))

# sql_membres = Table('membre', sql_meta, Column('membre_id',Integer, primary_key=True),      Column ('user_first_name', String), 
# Column ('user_last_name', String), Column ('email', String), Column ('phone_number', String), Column ('adresse', String), 
# Column ('zip_code', Integer), Column ('ville', String), Column ('canton', String), Column ('idt_file', String), 
# Column ('Read_and_accept', String), Column ('password', String), Column ('date_created', String))