from re import L

from wtforms import StringField, PasswordField, SubmitField, SelectField, MultipleFileField, TelField, IntegerField, BooleanField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email, NumberRange, InputRequired
from flask_wtf import FlaskForm


class RegistrationForm(FlaskForm):

    gender = SelectField(validators=[DataRequired()], choices=[
                         (None, 'Genre'), ('Femme', 'Femme'), ('Homme', 'Homme')])

    user_first_name = StringField(
        validators=[DataRequired(), Length(min=3, max=33)])

    user_last_name = StringField(
        validators=[DataRequired(), Length(min=3, max=33)])

    email = EmailField(validators=[DataRequired(), Email()])

    phone_number = TelField(
        validators=[DataRequired(), Length(min=10, max=33)])

    adresse = StringField(validators=[DataRequired(), Length(min=3, max=55)])

    zip_code = IntegerField(
        validators=[DataRequired(), NumberRange(min=1000, max=9658)])

    ville = StringField(validators=[DataRequired(), Length(min=2, max=36)])

    canton = SelectField(validators=[DataRequired()], choices=[('Vaud', 'Vaud'), ('Tessin', 'Tessin'), (
        'Neuchâtel', 'Neuchâtel'), ('Genève', 'Genève'), ('Valais', 'Valais'), ('Fribourg', 'Fribourg'), ('Jura', 'Jura')])

    file_id = MultipleFileField()

    Read_and_accept = BooleanField(
        validators=[DataRequired()])

    password = PasswordField(validators=[DataRequired(), Length(
        min=6, max=35), EqualTo('confirm_password')])

    confirm_password = PasswordField(
        validators=[DataRequired(), Length(
            min=6, max=35), EqualTo('password')])

    submit = SubmitField(label='Envoyez')


class LoginForm(FlaskForm):
    email = EmailField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[
                             DataRequired(), Length(min=6, max=35)])
    submit = SubmitField(label='Connexion')


class MailContactForm (FlaskForm):
    user_first_name = StringField(
        validators=[DataRequired(), Length(min=3, max=33)])

    user_last_name = StringField(
        validators=[DataRequired(), Length(min=3, max=33)])

    email = EmailField(validators=[DataRequired(), Email()])

    phone_number = TelField(
        validators=[DataRequired(), Length(min=10, max=33)])

    message_sent = TextAreaField(label='Message',
                                 validators=[DataRequired(), Length(min=1, max=1000)])

    submit = SubmitField(label='Envoyer')
