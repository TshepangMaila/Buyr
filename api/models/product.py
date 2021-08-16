from db import db

class Product(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.String(80))
    description = db.Column(db.String(80))
    type = db.Column(db.String(80))
    image_url = db.Column(db.String(80))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    user = db.relationship('User', back_populates='carts')
    cart = db.relationship('Cart', lazy='dynamic')

    def __init__(self, username, password):

        self.username = username
        self.password = password

    def json(self):
        return { "product_id" : self.id, "name" : self.name, "price" : self.price, "description" : self.desciption, "type" : self.type }

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
