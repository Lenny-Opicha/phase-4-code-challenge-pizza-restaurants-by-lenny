from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = "restaurants"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String)

    restaurant_pizzas = db.relationship("RestaurantPizza", backref="restaurant", cascade="all, delete-orphan")

    def to_dict(self):
        return {"id": self.id, "name": self.name, "address": self.address}


class Pizza(db.Model):
    __tablename__ = "pizzas"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String)

    restaurant_pizzas = db.relationship("RestaurantPizza", backref="pizza", cascade="all, delete-orphan")

    def to_dict(self):
        return {"id": self.id, "name": self.name, "ingredients": self.ingredients}


class RestaurantPizza(db.Model):
    __tablename__ = "restaurant_pizzas"
    
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizzas.id"), nullable=False)
    price = db.Column(db.Float)

    def to_dict(self):
        return {
            "id": self.id,
            "restaurant_id": self.restaurant_id,
            "pizza_id": self.pizza_id,
            "price": self.price,
        } 