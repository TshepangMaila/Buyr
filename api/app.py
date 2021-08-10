from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from routes import routes

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'buyrrr'

api = Api(app)

routes(api)

if __name__ == '__main__':
	app.run(port=5000)