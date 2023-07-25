from market import app 
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from market import db
from flask_login import login_user, logout_user, login_required

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/products')
@login_required
def products_page():
    products = Item.query.all()
    return render_template("products.html", itens=products)

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