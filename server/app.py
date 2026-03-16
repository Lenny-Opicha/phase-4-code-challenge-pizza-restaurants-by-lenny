from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

CORS(app)


@app.route('/')
def index():
    return {"message": "Pizza API running"}


# GET all restaurants
@app.route('/restaurants')
def restaurants():

    restaurants = Restaurant.query.all()

    restaurants_list = []

    for restaurant in restaurants:
        restaurants_list.append({
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
        })

    return jsonify(restaurants_list), 200


# GET single restaurant
@app.route('/restaurants/<int:id>')
def restaurant_by_id(id):

    restaurant = Restaurant.query.get(id)

    if not restaurant:
        return {"error": "Restaurant not found"}, 404

    pizzas = []

    for rp in restaurant.restaurant_pizzas:
        pizzas.append({
            "id": rp.pizza.id,
            "name": rp.pizza.name,
            "ingredients": rp.pizza.ingredients
        })

    restaurant_data = {
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "pizzas": pizzas
    }

    return jsonify(restaurant_data), 200


# GET all pizzas
@app.route('/pizzas')
def pizzas():

    pizzas = Pizza.query.all()

    pizza_list = []

    for pizza in pizzas:
        pizza_list.append({
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        })

    return jsonify(pizza_list), 200


# POST restaurant_pizzas
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():

    data = request.get_json()

    try:

        new_rp = RestaurantPizza(
            price=data["price"],
            pizza_id=data["pizza_id"],
            restaurant_id=data["restaurant_id"]
        )

        db.session.add(new_rp)
        db.session.commit()

        pizza = Pizza.query.get(data["pizza_id"])

        return jsonify({
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        }), 201

    except Exception as e:

        return {"errors": [str(e)]}, 400


if __name__ == '__main__':
    app.run(port=5555, debug=True) 