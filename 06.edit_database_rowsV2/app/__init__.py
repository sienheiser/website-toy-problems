from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

from app import database_model
from app import routes
