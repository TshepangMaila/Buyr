from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

from db import db

from routes import register_routes

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///buyr.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'buyrrr'

api = Api(app)

db.init_app(app)

@app.before_first_request
def create_tables():
	db.create_all()

register_routes(api=api)

if __name__ == '__main__':
	app.run(port=5000)