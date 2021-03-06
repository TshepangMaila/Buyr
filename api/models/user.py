from db import db

class User(db.Model):

	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80))
	email = db.Column(db.String(80))
	password = db.Column(db.String(80))
	role = db.Column(db.String(80))

	cart = db.relationship('Cart', lazy='dynamic')

	def __init__(self, email: str, username: str, password: str) -> None:

		self.email = email
		self.username = username
		self.password = password

	def save(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def find_by_email(cls, email):
		return cls.query.filter_by(email=email).first()

	@classmethod
	def find_by_username(cls, username):
		return cls.query.filter_by(username=username).first()

	@classmethod
	def find_by_id(cls, _id):
		return cls.query.filter_by(id=_id).first()