from project_f_h_c import app, db
from flask import render_template, url_for, redirect, flash, request
from flask_mail import Mail, Message
from project_f_h_c.forms import RegistrationForm, LoginForm, MailContactForm
from project_f_h_c.models import Membres


@app.route('/')
def accueilpage():
    return render_template('accueil.html', title="accueil")


@app.route('/activites')
def activitespage():
    return render_template('activites.html', title="activites")


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





app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'suisse1022@gmail.com'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_PASSWORD'] = 'ffyouafgwlovxvom'
mail = Mail(app)


def sendContactForm(result):
    msg = Message('Hello', sender="tampontimbre@gmail.com",
                  recipients=['suisse1022@gmail.com'])

    msg.body = """
    
    Hello There

    First Name: {}
    Last Name: {}
    Email: {}
    Phone Number {}
    Your message {}

    Salutation
    Sukru
    """.format(result['user_first_name'], result['user_last_name'], result['email'], result['phone_number'], result['message_sent'], result['user_first_name'])

    mail.send(msg)



@app.route('/contact', methods=['POST', 'GET'])
def contactpage():
    form=MailContactForm()
    if request.method == 'POST':
        result = {}
        result['user_first_name'] = request.form['user_first_name']
        result['user_last_name'] = request.form['user_last_name']
        result['email'] = request.form['email'].replace(' ', '')
        result['phone_number'] = request.form['phone_number']
        result['message_sent'] = request.form['message_sent']

        sendContactForm(result)
        return render_template('contact.html', title="Contact", form=form)
    return render_template('contact.html', title="Contact", form=form)
