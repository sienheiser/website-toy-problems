from app import app
from app.db_model import db,tbl1
from app.login import user_loader,request_loader,users,User
from sqlalchemy import select
from flask import render_template,request,redirect,url_for
from flask_login import login_user, login_required,logout_user,current_user

@app.route("/")
def index():
    return render_template("main.html")
@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/data")
@login_required
def data():
    query = select(tbl1)
    data = db.session.execute(query).scalars()
    return render_template('data.html',data = data)

@app.route("/login",methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        email = request.form['email']
        if email in users and request.form['password'] == users[email]['password']:
            user = User()
            user.id = email
            login_user(user)
            return render_template("submit.html",user=user.id)
        else:
            return 'Bad logic'

@app.route('/protected')
@login_required
def protected():
    return 'Logged in as: ' + current_user.id

@app.route('/logout')
def logout():
    logout_user()
    return render_template("main.html")
