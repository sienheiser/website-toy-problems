import os
from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

db_name = 'database/test.db'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR,db_name)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
db.init_app(app)

class tbl1(db.Model):
    __tablename__ = 'tbl1'
    rowid = db.Column(db.Integer, primary_key = True)
    one = db.Column(db.String)
    two = db.Column(db.Integer)
    def __repr__(self) -> str:
        return '<name {}>'.format(self.one)


