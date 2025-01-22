from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Homepage
@app.route('/')
def home():
    return render_template('home.html')

# Menu Page
@app.route('/menu')
def menu():
    menu_items = [
        {"id": 1, "name": "Margherita Pizza", "description": "Classic cheese and tomato base.", "price": 250, "image": "pizza.png"},
        {"id": 2, "name": "Chicken Burger", "description": "Grilled chicken patty with lettuce and mayo.", "price": 200, "image": "burger.png"},
        {"id": 3, "name": "Greek Salad", "description": "Fresh veggies with feta cheese.", "price": 150, "image": "salad.png"},
        {"id": 4, "name": "Pasta Alfredo", "description": "Creamy white sauce pasta.", "price": 300, "image": "pasta.png"},
        {"id": 5, "name": "Chocolate Cake", "description": "Rich and moist chocolate delight.", "price": 120, "image": "cake.png"},
        {"id": 6, "name": "Sneak", "description": "Delicious snack treat.", "price": 250, "image": "sneak.png"},
        {"id": 7, "name": "Sushi", "description": "Fresh and delicious sushi.", "price": 200, "image": "sushi.png"},
        {"id": 8, "name": "Ice Cream", "description": "Cool and creamy dessert.", "price": 150, "image": "icecream.png"},
        {"id": 9, "name": "Tacos", "description": "Spicy and crunchy tacos.", "price": 300, "image": "tacos.png"},
        {"id": 10, "name": "Pancake", "description": "Fluffy and sweet pancakes.", "price": 120, "image": "pancake.png"},
        {"id": 11, "name": "Dumpling", "description": "Soft and savory dumplings.", "price": 120, "image": "dumpling.png"}
    ]
    return render_template("menu.html", menu_items=menu_items)

# Order Page (Static, does not store data)
@app.route('/order/<int:item_id>')
def order(item_id):
    menu_items = [
        {"id": 1, "name": "Margherita Pizza", "price": 250},
        {"id": 2, "name": "Chicken Burger", "price": 200},
        {"id": 3, "name": "Greek Salad", "price": 150},
        {"id": 4, "name": "Pasta Alfredo", "price": 300},
        {"id": 5, "name": "Chocolate Cake", "price": 120},
    ]
    item = next((item for item in menu_items if item["id"] == item_id), None)
    if item:
        return render_template('order.html', item=item)
    return redirect(url_for('menu'))

# Success Page (Static)
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True)
