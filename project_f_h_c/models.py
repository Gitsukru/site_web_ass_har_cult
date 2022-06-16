# from project_f_h_c import db
# from datetime import datetime


# class Membres(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_first_name = db.Column(db.String(33), unique=True, nullable=False)
#     user_last_name = db.Column(db.String(33), unique=True, nullable=False)
#     email = db.Column(db.String(133), unique=True, nullable=False)
#     phone_number = db.Column(db.String(33), unique=True, nullable=False)
#     adresse = db.Column(db.String(33), unique=True, nullable=False)
#     zip_code = db.Column(db.String(33), unique=True, nullable=False)
#     ville = db.Column(db.String(33), unique=True, nullable=False)
#     canton = db.Column(db.String(33), unique=True, nullable=False)
#     idt_file = db.Column(db.String(133), nullable=False, default='default.jpg')
#     canton = db.Column(db.String(33), unique=True, nullable=False)
#     Read_and_accept = db.Column(db.Boolean(True), nullable=False)
#     password = db.Column(db.String(35), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return f'{self.user_first_name}: {self.user_last_name}: {self.email}: {self.phone_number}:{self.adresse}:{self.zip_code}:{self.ville}:{self.canton}:{self.date_created}'
