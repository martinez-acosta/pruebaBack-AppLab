from flask_pymongo import PyMongo

db = PyMongo()

def initialize_db(app):
    db.init_app(app)