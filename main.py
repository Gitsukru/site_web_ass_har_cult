# Python page main
from flask import Flask
from project_f_h_c import app


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
