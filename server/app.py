from flask import Flask, jsonify
from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route("/")
def home():
    return {"message": "Pizza API running"}


# GET /restaurants
@app.route("/restaurants")
def get_restaurants():
    restaurants = Restaurant.query.all()

    data = []

    for r in restaurants:
        data.append({
            "id": r.id,
            "name": r.name,
            "address": r.address
        })

    return jsonify(data)


# GET /pizzas
@app.route("/pizzas")
def get_pizzas():
    pizzas = Pizza.query.all()

    data = []

    for p in pizzas:
        data.append({
            "id": p.id,
            "name": p.name,
            "ingredients": p.ingredients
        })

    return jsonify(data)


# GET /restaurant_pizzas
@app.route("/restaurant_pizzas")
def get_restaurant_pizzas():
    restaurant_pizzas = RestaurantPizza.query.all()

    data = []

    for rp in restaurant_pizzas:
        data.append({
            "id": rp.id,
            "price": rp.price,
            "pizza_id": rp.pizza_id,
            "restaurant_id": rp.restaurant_id
        })

    return jsonify(data)


if __name__ == "__main__":
    app.run(port=5555) 