from project_f_h_c import app
from flask import render_template



@app.route('/')
@app.route('/accueil')
def accueilpage():
    return render_template('accueil.html', title="Accueil")

@app.route('/activites')
def activitespage():
    return render_template('activites.html', title="Activites")

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
