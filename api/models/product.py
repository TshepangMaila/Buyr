from db import db

class Product(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.String(80))
    description = db.Column(db.String(80))
    type = db.Column(db.String(80))
    image_url = db.Column(db.String(80))
    
    cart = db.relationship('Cart', lazy='dynamic')

    def __init__(self, name: str, price: float, desciption: str, type: str, image_url: str, user_id: int):

        self.name = name
        self.price = price
        self.description = desciption
        self.type = type
        self.image_url = image_url
        self.user_id = user_id

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
