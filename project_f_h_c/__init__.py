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


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'suisse1022@gmail.com'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_PASSWORD'] = 'ffyouafgwlovxvom'




# 2tables créer

# sql_membres = Table('membreTable', sql_meta, Column('membre_id',Integer, primary_key=True), Column ('user_first_name', String), 
# Column ('user_last_name', String), Column ('email', String), Column ('phone_number', String), Column ('adresse', String), 
# Column ('zip_code', Integer), Column ('ville', String), Column ('canton', String), Column ('idt_file', String), Column 
# ('Read_and_accept', String), Column ('password', String), Column ('date_created', String))

# sql_membres = Table('membres', sql_meta, Column('membre_id',Integer, primary_key=True),      Column ('user_first_name', String), 
# Column ('user_last_name', String), Column ('email', String), Column ('phone_number', String), Column ('adresse', String), 
# Column ('zip_code', Integer), Column ('ville', String), Column ('canton', String), Column ('idt_file', String), 
# Column ('Read_and_accept', String), Column ('password', String), Column ('date_created', String))