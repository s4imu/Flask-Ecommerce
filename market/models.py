from market import db, brcypt, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password = db.Column(db.String(length=60), nullable=False)
    cash = db.Column(db.Integer, nullable=False, default=5000)
    items = db.relationship('Item', backref='owner_user', lazy=True)

    @property
    def format_cash(self):
        if len(str(self.cash)) >= 4:
            return f'US$ {str(self.cash)[:-3]},{str(self.cash)[-3:]}'
        else:
            return f'US$ {self.cash}'

    @property  
    def crippassword(self):
        return self.crippassword
    
    @crippassword.setter
    def crippassword(self, password_text):
        self.password = brcypt.generate_password_hash(password_text).decode('utf-8')

    def decrypt_password(self, decrypted_password):
        return brcypt.check_password_hash(self.password, decrypted_password)

    def possible_purchase(self, product_obj):
        return self.cash >= product_obj.price
    def possible_return(self, product_obj):
        return product_obj in self.items
    
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))

    @property
    def format_price(self):
        if len(str(self.price)) >= 4:
            return f'US$ {str(self.price)[:-3]},{str(self.price)[-3:]}'
        else:
            return f'US$ {self.price}'
        
    def purchase(self, current_user):
        self.owner = current_user.id
        current_user.cash -= self.price
        db.session.commit()

    def return_product(self, current_user):
        self.owner = None
        current_user.cash += self.price
        db.session.commit()

  