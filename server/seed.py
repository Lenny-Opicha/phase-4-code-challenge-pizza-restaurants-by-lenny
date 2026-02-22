from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():
    # Delete existing data
    print("Deleting data...")
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()
    db.session.commit()

    # Create restaurants
    print("Creating restaurants...")
    shack = Restaurant(name="Shack", address="123 Main St")
    dominos = Restaurant(name="Dominos", address="456 Elm St")
    pizza_hut = Restaurant(name="Pizza Hut", address="789 Oak St")
    db.session.add_all([shack, dominos, pizza_hut])
    db.session.commit()

    # Create pizzas
    print("Creating pizzas...")
    cheese = Pizza(name="Cheese Pizza", ingredients="Cheese, Tomato Sauce, Dough")
    pepperoni = Pizza(name="Pepperoni Pizza", ingredients="Pepperoni, Cheese, Tomato Sauce, Dough")
    veggie = Pizza(name="Veggie Pizza", ingredients="Bell Peppers, Onions, Cheese, Tomato Sauce, Dough")
    db.session.add_all([cheese, pepperoni, veggie])
    db.session.commit()

    # Link restaurants and pizzas using relationship objects
    print("Creating RestaurantPizza associations...")
    rp1 = RestaurantPizza(price=5.99)
    rp1.restaurant = shack
    rp1.pizza = cheese

    rp2 = RestaurantPizza(price=6.99)
    rp2.restaurant = shack
    rp2.pizza = pepperoni

    rp3 = RestaurantPizza(price=6.49)
    rp3.restaurant = dominos
    rp3.pizza = cheese

    rp4 = RestaurantPizza(price=6.99)
    rp4.restaurant = dominos
    rp4.pizza = veggie

    rp5 = RestaurantPizza(price=7.49)
    rp5.restaurant = pizza_hut
    rp5.pizza = pepperoni

    rp6 = RestaurantPizza(price=7.99)
    rp6.restaurant = pizza_hut
    rp6.pizza = veggie

    db.session.add_all([rp1, rp2, rp3, rp4, rp5, rp6])
    db.session.commit()

    print("Seeding complete!") 