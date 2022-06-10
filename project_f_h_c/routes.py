from project_f_h_c import app
from flask import render_template, url_for, redirect, flash
from project_f_h_c.forms import RegistrationForm, LoginForm

# @app.route('/')


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
        flash(
            f'Compte a été créer avec succès pour{form.user_first_name.data}', category='success')
        return redirect(url_for('loginpage'))
    return render_template('register.html', title="Inscription", form=form)


@app.route('/login', methods=['POST', 'GET'])
def loginpage():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'aaa@sss.com' and form.password.data == '123456':
            flash(
                f'Connexion avec succès pour{form.email.data}', category='success')
            return redirect(url_for('accountpage'))
        else:
            flash(
                f'Echec de la connexion pour{form.email.data}', category='danger')
    return render_template('login.html', title="Connexion", form=form)
