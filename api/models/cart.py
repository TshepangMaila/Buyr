from db import db

class Cart(db.Model):

	__tablename__ = 'carts'

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
	
	product = db.relationship('Product', back_populates='carts')
	user = db.relationship('User', back_populates='carts')

	def __init__(self, username, password):

		self.username = username
		self.password = password

	def save(self):
		db.session.add(self)
		db.session.commit()

	def delete(self):
		db.session.delete(self)
		db.session.commit()

	@classmethod
	def find_by_user_id(cls, _id):
		return cls.query.filter_by(user_id=_id).first()

	@classmethod
	def find_by_product_id(cls, _id):
		return cls.query.filter_by(product_id=_id).first()