from app import app
from flask import render_template

@app.route("/")
def index():
    li = [1,2,3,4]
    return render_template("table.html",li=li)

