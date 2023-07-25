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
    itens = db.relationship('Item', backref='owner_user', lazy=True)

    @property
    def format_cash(self):
        if len(str(self.cash)) >= 4:
            return f'R$ {str(self.cash)[:-3]},{str(self.cash)[-3:]}'
        else:
            return f'R$ {self.cash}'

    @property  
    def crippassword(self):
        return self.crippassword
    
    @crippassword.setter
    def crippassword(self, password_text):
        self.password = brcypt.generate_password_hash(password_text).decode('utf-8')

    def decrypt_password(self, decrypted_password):
        return brcypt.check_password_hash(self.password, decrypted_password)

    def __repr__(self):
        return f"\nUser: {self.user}, Email: {self.email}, Password: {self.password}, Cash: {self.cash}"

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"\nName: {self.name}, Price: {self.price}, Barcode: {self.barcode}, Description: {self.description}"
