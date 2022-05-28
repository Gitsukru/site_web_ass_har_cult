from flask import Flask
from project_f_h_c import app


def test_app():
    print ("Testing app")


if __name__ == '__main__':
    app.run(debug=True)