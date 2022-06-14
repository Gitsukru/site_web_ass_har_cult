from project_f_h_c import app, db
from flask import render_template, url_for, redirect, flash
from project_f_h_c.forms import RegistrationForm, LoginForm
from project_f_h_c.models import Membres


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
        membres = Membres(user_first_name=form.user_first_name.data, user_last_name=form.user_last_name.data, email=form.email.data, phone_number=form.phone_number.data,
                          adresse=form.adresse.data, zip_code=form.zip_code.data, ville=form.ville.data, canton=form.canton.data, password=form.password.data)
        db.session.add(membres)
        db.session.commit()
        flash(
            f'Compte a été créer avec succès pour {form.user_first_name.data}', category='success')
        # print("Register page to login")
        return redirect(url_for('loginpage'))

    return render_template('register.html', title="Inscription", form=form)


@app.route('/login', methods=['POST', 'GET'])
def loginpage():
    form = LoginForm()
    # print("form Login !!!")
    if form.validate_on_submit():
        print("sous submit")
        if form.email.data == 'aaa@gmail.com' and form.password.data == '123456':
            flash(
                f'Connexion avec succès pour {form.email.data}', category='success')
            # print("sous flasch")
            return redirect(url_for('accountpage'))
        else:
            flash(
                f'Echec de la connexion pour {form.email.data}', category='danger')
            # print("pas pu connecter")
    return render_template('login.html', title="Connexion", form=form)
