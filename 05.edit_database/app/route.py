from app import app
from app.database_model import tbl1,db
from flask import render_template,request
from sqlalchemy import select,update


@app.route('/',methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        val = request.form['one']
        query = update(tbl1).where(tbl1.rowid == 1).values(one = val)
        db.session.flush()
        db.session.commit()
        query = db.select(tbl1)
        data = db.session.execute(query).scalars()
        return render_template("data_dynamic.html",data = data)
    else:
        query = select(tbl1.one,tbl1.two)
        data = db.session.execute(query)
        return render_template('data.html',data = data)
