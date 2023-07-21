from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/products')
def products_page():
    products = [
        {'id': 1, 'name': 'cellphone', 'barcode': '123789', 'price': 1200},
        {'id': 2, 'name': 'laptop', 'barcode': '113784', 'price': 2400},
        {'id': 3, 'name': 'fridge', 'barcode': '125186', 'price': 1650},
        {'id': 4, 'name': 'television', 'barcode': '163719', 'price': 3000}
    ]
    return render_template("products.html", itens=products)


@app.route('/login')
def login_page():

    return render_template("login.html")

@app.route('/signup')
def signup_page():

    return render_template("signup.html")