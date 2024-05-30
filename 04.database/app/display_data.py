import os
from app import app,db
from app.database_model import tbl1 
from flask import render_template
from sqlalchemy import select


@app.route('/')
def index():
    query = select(tbl1.one,tbl1.two)
    data = db.session.execute(query)
    return render_template('table.html', data=data)
