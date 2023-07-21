from market import app 
from flask import render_template
from market.models import Item

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/products')
def products_page():
    products = Item.query.all()
    return render_template("products.html", itens=products)

@app.route('/login')
def login_page(): 
    return render_template("login.html")

@app.route('/signup')
def signup_page():
    return render_template("signup.html")