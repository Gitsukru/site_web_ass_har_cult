from project_f_h_c import app, db
from flask import render_template, url_for, redirect, flash
from project_f_h_c.forms import RegistrationForm, LoginForm
from project_f_h_c.models import Membres



# from datetime import datetime

# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import MetaData
# from sqlalchemy import create_engine
# from sqlalchemy import Column
# from sqlalchemy import Table
# from sqlalchemy import Integer
# from sqlalchemy import String
# from datetime import datetime


@app.route('/')
def accueilpage():
    return render_template('accueil.html', title="accueil")


@app.route('/activites')
def activitespage():
    return render_template('activites.html', title="activites")


@app.route('/contact')
def contactpage():
    return render_template('contact.html', title="Contact")


@app.route('/cours')
def courspage():
    return render_template('cours.html', title="Cours")


@app.route('/donation')
def donationpage():
    return render_template('donation.html', title="Donation")


@app.route('/membres')
def membrespage():
    return render_template('membres.html', title="Membres")


@app.route('/account')
def accountpage():
    return render_template('account.html', title="Account")


@app.route('/register', methods=['POST', 'GET'])
def registerpage():
    form = RegistrationForm()
    if form.validate_on_submit():
        membre = Membres(user_first_name=form.user_first_name.data, user_last_name=form.user_last_name.data, email=form.email.data, phone_number=form.phone_number.data,
                         adresse=form.adresse.data, zip_code=form.zip_code.data, ville=form.ville.data, canton=form.canton.data, password=form.password.data)
        db.session.add(membre)
        db.session.commit()
        flash(
            f'Compte a été créer avec succès pour {form.user_first_name.data}', category='success')
        return redirect(url_for('loginpage'))

    return render_template('register.html', title="Inscription", form=form)


@app.route('/login', methods=['POST', 'GET'])
def loginpage():
    form = LoginForm()
    if form.validate_on_submit():
        membre = Membres.query.filter_by(email=form.email.data).first()
        if form.email.data == membre.email and form.password.data == membre.password:
            flash(
                f'Connexion avec succès pour {form.email.data}', category='success')
            return redirect(url_for('accountpage'))
        else:
            flash(
                f'Echec de la connexion pour {form.email.data}', category='danger')
    return render_template('login.html', title="Connexion", form=form)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/sukru/Ada_Flow/Projet_Final_Harmonie_Culturelle/project_f_h_c/hrmcultdb.db'
# db = SQLAlchemy(app)
# db.init_app(app)
# db.create_all()
# app.config['SECRET_KEY'] = 'firstloginflask'
# sql_uri = 'sqlite:///db.sqlite'
# sql_engine = create_engine(sql_uri)
# sql_meta = MetaData(sql_engine)


# class Membres(db.ModeL):
#     id = db.Column(db.Integer, primary_key=True)
#     user_first_name = db.Column(db.String(33), unique=True, nullable=False)
#     user_last_name = db.Column(db.String(33), unique=True, nullable=False)
#     email = db.Column(db.String(133), unique=True, nullable=False)
#     phone_number = db.Column(db.String(33), unique=True, nullable=False)
#     adresse = db.Column(db.String(33), unique=True, nullable=False)
#     zip_code = db.Column(db.Integer(33), unique=True, nullable=False)
#     ville = db.Column(db.String(33), unique=True, nullable=False)
#     canton = db.Column(db.String(33), unique=True, nullable=False)
#     idt_file = db.Column(db.String(133), nullable=False, default='default.jpg')
#     Read_and_accept = db.Column(db.Boolean(True), nullable=False)
#     password = db.Column(db.String(35), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self, user_first_name, user_last_name, email, phone_number, adresse, zip_code, ville, canton, date_created, idt_file, Read_and_accept, password):
#         self.user_first_name = user_first_name
#         self.user_last_name = user_last_name
#         self.email = email
#         self.phone_number = phone_number
#         self.adresse = adresse
#         self.zip_code = zip_code
#         self.ville = ville
#         self.canton = canton
#         self.idt_file = idt_file
#         self.Read_and_accept = Read_and_accept
#         self.password = password
#         self.date_created = date_created
