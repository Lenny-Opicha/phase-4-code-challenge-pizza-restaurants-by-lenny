from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():

    print("Deleting old data...")
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()

    print("Creating restaurants...")

    r1 = Restaurant(
        name="Karen's Pizza Shack",
        address="123 Nairobi Street"
    )

    r2 = Restaurant(
        name="Lenny's Italian Spot",
        address="456 Kampala Avenue"
    )

    print("Creating pizzas...")

    p1 = Pizza(
        name="Margherita",
        ingredients="Tomato, Mozzarella, Basil"
    )

    p2 = Pizza(
        name="Pepperoni",
        ingredients="Tomato, Mozzarella, Pepperoni"
    )

    print("Creating restaurant pizzas...")

    rp1 = RestaurantPizza(
        price=10,
        pizza=p1,
        restaurant=r1
    )

    rp2 = RestaurantPizza(
        price=15,
        pizza=p2,
        restaurant=r1
    )

    rp3 = RestaurantPizza(
        price=18,
        pizza=p2,
        restaurant=r2
    )

    db.session.add_all([r1, r2, p1, p2, rp1, rp2, rp3])
    db.session.commit()

    print("Seeding complete!") 