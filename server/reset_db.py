from app import app, db
from models import Restaurant, Pizza, RestaurantPizza

# Drop all tables and recreate them to match current models
with app.app_context():
    db.drop_all()
    db.create_all()

    # Seed Restaurants
    r1 = Restaurant(name="Shelly Figueroa", address="75839 Valenzuela Crescent Apt. 012 North Angelafort")
    r2 = Restaurant(name="Jody Anderson", address="803 Lisa Roads Camposchester")

    db.session.add_all([r1, r2])
    db.session.commit()

    # Seed Pizzas
    p1 = Pizza(name="Margherita", ingredients="tomato, mozzarella, basil")
    p2 = Pizza(name="Pepperoni", ingredients="tomato, mozzarella, pepperoni")
    p3 = Pizza(name="Hawaiian", ingredients="tomato, mozzarella, ham, pineapple")

    db.session.add_all([p1, p2, p3])
    db.session.commit()

    # Seed RestaurantPizza with valid prices
    rp1 = RestaurantPizza(price=12, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=15, restaurant_id=r1.id, pizza_id=p2.id)
    rp3 = RestaurantPizza(price=20, restaurant_id=r2.id, pizza_id=p2.id)
    rp4 = RestaurantPizza(price=25, restaurant_id=r2.id, pizza_id=p3.id)

    db.session.add_all([rp1, rp2, rp3, rp4])
    db.session.commit()

    print("Database seeded with restaurants, pizzas, and restaurant_pizzas!") 