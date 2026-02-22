import requests

BASE_URL = "http://127.0.0.1:5555"

def test_restaurants():
    print("Testing GET /restaurants")
    r = requests.get(f"{BASE_URL}/restaurants")
    print(f"Status Code: {r.status_code}")
    print(r.text)
    print("-" * 50)

    print("Testing POST /restaurants")
    r = requests.post(f"{BASE_URL}/restaurants", json={"name": "Test Restaurant"})
    print(f"Status Code: {r.status_code}")
    print(r.json())
    print("-" * 50)

def test_pizzas():
    print("Testing GET /pizzas")
    r = requests.get(f"{BASE_URL}/pizzas")
    print(f"Status Code: {r.status_code}")
    print(r.text)
    print("-" * 50)

    print("Testing POST /pizzas")
    r = requests.post(f"{BASE_URL}/pizzas", json={"name": "Test Pizza", "ingredients": "Cheese, Tomato"})
    print(f"Status Code: {r.status_code}")
    print(r.json())
    print("-" * 50)

def test_restaurant_pizzas():
    print("Testing GET /restaurant_pizzas")
    r = requests.get(f"{BASE_URL}/restaurant_pizzas")
    print(f"Status Code: {r.status_code}")
    print(r.text)
    print("-" * 50)

    print("Testing POST /restaurant_pizzas")
    # Make sure you have at least one restaurant and pizza in DB before testing
    r = requests.post(f"{BASE_URL}/restaurant_pizzas", json={"restaurant_id": 1, "pizza_id": 1, "price": 9.99})
    print(f"Status Code: {r.status_code}")
    print(r.json())
    print("-" * 50)

if __name__ == "__main__":
    test_restaurants()
    test_pizzas()
    test_restaurant_pizzas() 