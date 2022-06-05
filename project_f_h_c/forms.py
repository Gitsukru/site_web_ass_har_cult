from flask_wtf import FlaskForm
# import re
# re.compile(u'^[^/\\]\.jpg$')
from wtforms import StringField, PasswordField, SubmitField, SelectField, FileField, TelField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class RegistrationForm(FlaskForm):
    user_first_name = StringField(label='User first name', validators=[DataRequired(), Length(min='3', max='33')])
    user_last_name = StringField(label='User last name', validators=[DataRequired(), Length(min='3', max='33')])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    phone_number = TelField(label='Phone Number', validators=[DataRequired(),])
    adresse = StringField(label='Adresse', validators=[DataRequired(), Length(min='3', max='55')])
    zip_code = IntegerField(label='CP', validators=[DataRequired(), Length(min='4', max='6')])
    password = PasswordField(label='Password', validators=[DataRequired(),Length(min='6', max='20')])
    confirm_password = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label='Envoyez')



class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(),Length(min='6', max='20')])
    submit = SubmitField(label='Login')

