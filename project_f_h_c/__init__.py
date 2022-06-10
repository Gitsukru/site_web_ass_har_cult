from flask import Flask

app=Flask(__name__)

app.config['SECRET_KEY'] ='firstloginflask'

from project_f_h_c import routes