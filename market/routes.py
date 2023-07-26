from market import app 
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, BuyProductForm, SaleProductForm
from market import db
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/products', methods=['GET', 'POST'])
@login_required
def products_page():
    buy_form = BuyProductForm()
    if request.method == "POST":
        buy_product = request.form.get("buy_product")
        product_obj = Item.query.filter_by(name=buy_product).first()
        if product_obj:
            if current_user.possible_purchase(product_obj):
                product_obj.purchase(current_user)
                flash(f"{product_obj.name} Successfully Purchased!!!", category="success")
            else:
                flash(f"Purchase of {product_obj.name} not made due to lack of balance", category="danger")
        return redirect(url_for('products_page'))
    if request.method == "GET":
        products = Item.query.filter_by(owner=None)
        return render_template("products.html", itens=products, buy_form=buy_form)

@app.route('/login', methods=['GET', 'POST'])
def login_page(): 
    form = LoginForm()
    if form.validate_on_submit():
        logged_user = User.query.filter_by(user=form.user.data).first()
        if logged_user and logged_user.decrypt_password(decrypted_password=form.password.data):
            login_user(logged_user)
            flash(f'Successful Login. Welcome {logged_user.user}', category="success")
            return redirect(url_for('products_page'))
        else:
            flash(f'Incorrect username or password! Try again.', category="danger")
    return render_template("login.html", form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(
            user = form.user.data,
            email = form.email.data,
            crippassword = form.password1.data
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('products_page'))
    
    if form.errors != {}:
        for err in form.errors.values():
            flash(f"Error in register user {err}", category="danger")

    return render_template("signup.html", form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You've been logged out", category="info")

    return redirect(url_for("home_page"))