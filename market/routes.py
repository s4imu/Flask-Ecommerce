from market import app 
from flask import render_template, redirect, url_for
from market.models import Item, User
from market.forms import RegisterForm
from market import db

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

@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(
            user = form.user.data,
            email = form.email.data,
            password = form.password1.data
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('products_page'))

    return render_template("signup.html", form=form)