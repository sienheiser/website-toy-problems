from app import app
from sqlalchemy import select,update
from app.database_model import db, tbl1
from flask import render_template,request

@app.route('/')
def index():
    query = select(tbl1.rowid,tbl1.col1,tbl1.col2)
    data = db.session.execute(query)
    return render_template("data/data.html",data = data)

@app.route('/edit/<int:id>')
def edit(id:int):
    query = select(tbl1.col1,tbl1.col2).where(tbl1.rowid == id)
    data = db.session.execute(query)
    return render_template("data/data_edit_row_view.html",data = data,id = id)

def parse(data:bytes) -> list:
    data_str = str(data).replace("'","")
    data_str.replace("%20"," ")
    split_data = data_str.split("&")
    values = []
    for i in range(len(split_data)):
        index = split_data[i].find("=")
        val = split_data[i][index+1:]
        if val.isdigit():
            values.append(int(val))
        else:
            values.append(val)
    print(values)
    return values 
@app.route('/cancel/<int:id>',methods = ['GET','POST'])
def cancel(id:int):
    if request.method == 'POST':
        data = parse(request.get_data())
        cols = ["col1","col2"]
        for i in range(len(cols)):
            col = cols[i]
            print(col,data[i])
            values = {col: data[i]}
            query=update(tbl1).where(tbl1.rowid == id).values(**values)
            db.session.execute(query)
            db.session.commit()
        final_query =  select(tbl1).where(tbl1.rowid == id)
        data = db.session.execute(final_query).scalars()
        return render_template("data/data_normal_row.html",data = data , id = id) 
    else:
        query = select(tbl1.col1,tbl1.col2).where(tbl1.rowid == id)
        data = db.session.execute(query)
        return render_template("data/data_normal_row.html",data = data,id = id)
