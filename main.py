from flask import Flask, render_template,request,session
import json
import urllib.request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db= SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Email = db.Column(db.Text)
    Password = db.Column(db.Integer)
    Age = db.Column(db.Integer)
    Server = db.Column(db.Text)
    Timing = db.Column(db.Text)
    About = db.Column(db.Text)
    db.create_all()


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
    user = User(Email=email, Password=password,Age=None, Server = None, Timing = None)
    existing_user = User.query.filter_by(Email=email).first()
    pasword_checker = User.query.filter_by(Password=password).first()
    print(existing_user)
    print(pasword_checker)
    if existing_user is None or pasword_checker is None:
        return 'invalid creds'
    else:
        return render_template("home.html")  
        

    



@app.route("/sign", methods = ['POST'])
def register():
    print("hello there")
    email = request.form['email']
    password = request.form['psw']
    repeat = request.form['psw-repeat']
    user = User(Email=email, Password=password)
    print(user)
    existing_user = User.query.filter_by(Email=email).first()

    if password != repeat or existing_user is not None:
        return 'invalid credentials the email used may have already been in use or your repeat and original passswords are different '
    elif password==repeat:
        db.create_all()
        db.session.add(user)
        db.session.commit()
        return render_template("home.html") 



@app.route("/data", methods = ['POST'])
def data():
    print("hello there")
    email = request.form['email']
    password = request.form['psw']
    repeat = request.form['psw-repeat']
    user = User(Email=email, Password=password)
    print(user)
    existing_user = User.query.filter_by(Email=email).first()

    if password != repeat or existing_user is not None:
        return 'invalid credentials the email used may have already been in use or your repeat and original passswords are different '
    elif password==repeat:
        db.create_all()
        db.session.add(user)
        db.session.commit()
        return render_template("home.html") 


@app.route("/home")
def home():
    email = request.form['email']
    bday = request.form['bdate']
    time = request.form['time']
    server = request.form['server']
    about = request.form['about']
    user = User(Email=Email, Age = bday, Server=Server, Timing=Time, About=about )

    return render_template("home.html")



if __name__ == '__main__':
    app.run(debug=True)
