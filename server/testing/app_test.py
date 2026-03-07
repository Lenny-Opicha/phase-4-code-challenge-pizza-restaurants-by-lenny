from flask import Flask, jsonify
from db import db
from models import Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# ------------------------------
# Routes
# ------------------------------

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{
        "id": r.id,
        "name": r.name,
        "address": r.address
    } for r in restaurants]), 200


@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "ingredients": p.ingredients
    } for p in pizzas]), 200


@app.route('/restaurant_pizzas', methods=['GET'])
def get_restaurant_pizzas():
    rps = RestaurantPizza.query.all()
    return jsonify([{
        "id": rp.id,
        "price": rp.price,
        "restaurant_id": rp.restaurant_id,
        "pizza_id": rp.pizza_id
    } for rp in rps]), 200


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 