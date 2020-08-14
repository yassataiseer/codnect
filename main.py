from flask import Flask, render_template,request,session
import json
import urllib.request
from flask_sqlalchemy import SQLAlchemy
from mailer import deliver
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db= SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Email = db.Column(db.Text)
    Password = db.Column(db.Integer)


@app.route("/")
def index():
    return render_template("sign-up.html")


@app.route("/signup")
def index1():
    return render_template("sign-up.html")


@app.route("/login")
def login():

    return render_template("login.html")
    

@app.route("/logger", methods = ['POST'])
def log():
    email = request.form['emailer']
    password = request.form['pswrd']
    existing_user = User.query.filter_by(Email=email).first()
    pasword_checker = User.query.filter_by(Password=password).first()
    print(existing_user)
    print(pasword_checker)
    if existing_user is not None or pasword_checker is not None or username==''or password=='' :
        return render_template("index.html")    
    else:
        return 'invalid creds'

    



@app.route("/sign", methods = ['POST'])
def register():
    print("hello there")
    email = request.form['email']
    password = request.form['psw']
    repeat = request.form['psw-repeat']
    user = User(Email=email, Password=password)
    print(user)
    if password != repeat :
        return 'invalid credentials '
    elif password==repeat:
        db.create_all()
        db.session.add(user)
        db.session.commit()
        return render_template("index.html") 


if __name__ == '__main__':
    app.run(debug=True)
