from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timezone, datetime


""" create a SQLAlchemy instance to handle the database"""
db = SQLAlchemy()


class User(db.Model):
    """ this is the table name in the database"""
    __tablename__ = 'users'

    """unique id for each users"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    """storing hashed password"""
    password_hash = db.Column(db.String(128), nullable=False)
    """Timestamp"""
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    portfolios = db.relationship('Portfolio', backref='owner', lazy=True)

    """ Password handling"""
    def set_password(self, password):
        """ hash the password"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """check if the password is hash"""
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return  f'<User {self.username}>'
    

class Portfolio(db.Model):
    __tablename__ = 'portfolios'

    id = db.Column(db.Integer, primary_key=True)
    """Links to the user"""
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    """e.g aapl for applestock"""
    stock_symbol = db.Column(db.String(10), nullable=False)
    """number of shares owned"""
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    user = db.relationship('User', backref=db.backref('portfolios', lazy=True))


    def __repr__(self):
        return f'<Portfolio {self.stock_symbol}: {self.quantity}>'
    

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    stock_symbol = db.Column(db.String(10), nullable=False)
    """ positive for buy negative for sell"""
    quantity = db.Column(db.Integer, nullable=False)
    """" price of stock at the time"""
    price_per_share = db.Column(db.Float, nullable=False)
    """ when the transcarion happened """
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    user = db.relationship('User', backref=db.backref('transactions', lazy=True))

    def __repr__(self):
        return f'<Transaction {self.stock_symbol} {self.quantity}'