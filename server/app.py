#!/usr/bin/env python3
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Restaurant, Pizza, RestaurantPizza
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def index():
    return "<h1>Code challenge</h1>"

# ---------------- Restaurants ----------------
@app.route("/restaurants", methods=["GET", "POST"])
def handle_restaurants():
    if request.method == "GET":
        return jsonify([r.to_dict() for r in Restaurant.query.all()]), 200
    data = request.get_json() or {}
    new_restaurant = Restaurant(name=data.get("name", "Test Restaurant"), address=data.get("address"))
    db.session.add(new_restaurant)
    db.session.commit()
    return jsonify(new_restaurant.to_dict()), 201

# ---------------- Pizzas ----------------
@app.route("/pizzas", methods=["GET", "POST"])
def handle_pizzas():
    if request.method == "GET":
        return jsonify([p.to_dict() for p in Pizza.query.all()]), 200
    data = request.get_json() or {}
    new_pizza = Pizza(name=data.get("name", "Test Pizza"), ingredients=data.get("ingredients"))
    db.session.add(new_pizza)
    db.session.commit()
    return jsonify(new_pizza.to_dict()), 201

# ---------------- RestaurantPizza ----------------
@app.route("/restaurant_pizzas", methods=["GET", "POST"])
def handle_restaurant_pizzas():
    if request.method == "GET":
        return jsonify([rp.to_dict() for rp in RestaurantPizza.query.all()]), 200
    
    # Parse JSON safely
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON body required"}), 400

    restaurant_id = data.get("restaurant_id")
    pizza_id = data.get("pizza_id")
    price = data.get("price", 0)

    # Validate IDs exist
    restaurant = Restaurant.query.get(restaurant_id)
    pizza = Pizza.query.get(pizza_id)
    if not restaurant or not pizza:
        return jsonify({"error": "Invalid restaurant_id or pizza_id"}), 400

    new_rp = RestaurantPizza(
        restaurant_id=restaurant_id,
        pizza_id=pizza_id,
        price=price
    )
    db.session.add(new_rp)
    db.session.commit()
    return jsonify(new_rp.to_dict()), 201