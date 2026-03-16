from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

db = SQLAlchemy()


class Restaurant(db.Model):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    restaurant_pizzas = db.relationship(
        "RestaurantPizza",
        back_populates="restaurant",
        cascade="all, delete-orphan"
    )

    pizzas = association_proxy("restaurant_pizzas", "pizza")


class Pizza(db.Model):
    __tablename__ = "pizzas"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)

    restaurant_pizzas = db.relationship(
        "RestaurantPizza",
        back_populates="pizza",
        cascade="all, delete-orphan"
    )

    restaurants = association_proxy("restaurant_pizzas", "restaurant")


class RestaurantPizza(db.Model):
    __tablename__ = "restaurant_pizzas"

    id = db.Column(db.Integer, primary_key=True)

    price = db.Column(db.Integer, nullable=False)

    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"))
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizzas.id"))

    restaurant = db.relationship("Restaurant", back_populates="restaurant_pizzas")
    pizza = db.relationship("Pizza", back_populates="restaurant_pizzas")

    @validates("price")
    def validate_price(self, key, value):
        if value < 1 or value > 30:
            raise ValueError("Price must be between 1 and 30")
        return value 