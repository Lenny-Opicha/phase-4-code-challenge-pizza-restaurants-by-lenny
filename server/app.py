from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

CORS(app)

db.init_app(app)


@app.route("/")
def index():
    return {"message": "Pizza API running"}


# ----------------------------
# GET ALL RESTAURANTS
# ----------------------------
@app.route("/restaurants", methods=["GET"])
def get_restaurants():

    restaurants = Restaurant.query.all()

    return jsonify([
        {
            "id": r.id,
            "name": r.name,
            "address": r.address
        }
        for r in restaurants
    ]), 200


# ----------------------------
# GET RESTAURANT BY ID
# ----------------------------
@app.route("/restaurants/<int:id>", methods=["GET"])
def get_restaurant(id):

    restaurant = Restaurant.query.get(id)

    if not restaurant:
        return {"error": "Restaurant not found"}, 404

    return {
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "pizzas": [
            {
                "id": p.id,
                "name": p.name,
                "ingredients": p.ingredients
            }
            for p in restaurant.pizzas
        ]
    }, 200


# ----------------------------
# DELETE RESTAURANT
# ----------------------------
@app.route("/restaurants/<int:id>", methods=["DELETE"])
def delete_restaurant(id):

    restaurant = Restaurant.query.get(id)

    if not restaurant:
        return {"error": "Restaurant not found"}, 404

    db.session.delete(restaurant)
    db.session.commit()

    return "", 204


# ----------------------------
# GET ALL PIZZAS
# ----------------------------
@app.route("/pizzas", methods=["GET"])
def get_pizzas():

    pizzas = Pizza.query.all()

    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "ingredients": p.ingredients
        }
        for p in pizzas
    ]), 200


# ----------------------------
# CREATE RESTAURANT PIZZA
# ----------------------------
@app.route("/restaurant_pizzas", methods=["POST"])
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
        restaurant = Restaurant.query.get(data["restaurant_id"])

        return {
            "id": new_rp.id,
            "price": new_rp.price,
            "pizza": {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            },
            "restaurant": {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address
            }
        }, 201

    except Exception:
        return {"errors": ["validation errors"]}, 400


if __name__ == "__main__":
    app.run(port=5555, debug=True) 