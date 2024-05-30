from flask import Flask
app = Flask(__name__)
app.secret_key = 'super secret string'

from app import routes
from app import db_model
from app import login
