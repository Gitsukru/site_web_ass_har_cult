
from project_f_h_c import app, db
from datetime import datetime


from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import Integer
from sqlalchemy import String


sql_uri = 'sqlite:///project_f_h_c/database/db.sqlite'

sql_engine = create_engine(sql_uri)
sql_meta = MetaData(sql_engine)


class Membres(db.Model):
    membre_id = db.Column(db.Integer, primary_key=True)
    user_first_name = db.Column(db.String(33), unique=True, nullable=False)
    user_last_name = db.Column(db.String(33), unique=True, nullable=False)
    email = db.Column(db.String(133), unique=True, nullable=False)
    phone_number = db.Column(db.String(33), unique=True, nullable=False)
    adresse = db.Column(db.String(33), unique=True, nullable=False)
    zip_code = db.Column(db.String(33), unique=True, nullable=False)
    ville = db.Column(db.String(33), unique=True, nullable=False)
    canton = db.Column(db.String(33), unique=True, nullable=False)
    idt_file = db.Column(db.String(133), nullable=False, default='default.jpg')
    Read_and_accept = db.Column(db.Boolean(True), nullable=False)
    password = db.Column(db.String(35), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self,user_first_name, user_last_name, email, phone_number, adresse, zip_code, ville, canton, date_created, idt_file, Read_and_accept, password):
        self.user_first_name = user_first_name
        self.user_last_name = user_last_name
        self.email = email
        self.phone_number = phone_number
        self.adresse = adresse
        self.zip_code = zip_code
        self.ville = ville
        self.canton = canton
        self.idt_file = idt_file
        self.Read_and_accept = Read_and_accept
        self.password = password
        self.date_created = date_created

    # def validate_unique_email(self, email):
    #     if db.Model.email == email.data:
    #         raise ValidationError('Cette email est déjà enregistrer.')