from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():

    db.drop_all()
    db.create_all()

    r1 = Restaurant(
        name="Shelly Figueroa",
        address="75839 Valenzuela Crescent Apt. 012 North Angelafort"
    )
    r2 = Restaurant(
        name="Jody Anderson",
        address="803 Lisa Roads Camposchester"
    )

    p1 = Pizza(
        name="Margherita",
        ingredients="Cheese, Tomato"
    )

    p2 = Pizza(
        name="Pepperoni",
        ingredients="Cheese, Pepperoni"
    )

    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    print("Database seeded successfully!") 