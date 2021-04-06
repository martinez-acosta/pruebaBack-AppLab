from flask import Flask, jsonify, request, make_response, Response
from flask_cors import CORS
from flask_pymongo import PyMongo
import os
from api import api
from config.database import initialize_db

app = Flask(__name__)
app.config.from_pyfile(os.path.join(".", "config/app.conf"), silent=False)

mongo = PyMongo(app)
CORS(app, resources={r'/*': {'origins': '*'}})
initialize_db(app)
api.init_app(app)

if __name__=='__main__':
  app.run(debug=True)
