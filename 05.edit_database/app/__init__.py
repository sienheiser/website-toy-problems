from flask import Flask
app = Flask(__name__)

from app import route
from app import database_model


