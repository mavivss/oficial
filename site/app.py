from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/doacoes')
def doacoes():
    return render_template('/doacoes.html')


@app.route('/cadastre')
def cadastre():
    return render_template('/cadastre.html')


@app.route('/login')
def login():
    return render_template('/login.html')




if __name__ == "__main__":
   app.run(debug=True)
