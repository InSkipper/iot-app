from . import db

from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    login = db.Column(db.String(100))
    hub_ip = db.Column(db.String(15), unique=True)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    temperature = db.Column(db.Float)
    pressure = db.Column(db.Float)
    humidity = db.Column(db.Float)
    co2 = db.Column(db.Float)
    time = db.Column(db.DateTime)

    # # Many to one
    # class Hub(db.Model):
    #     id = db.Column(db.Integer, primary_key=True)
    #     # owner = db.Column(db.String(100), secondary_key=True)  # Same as name in User
    #     ip = db.Column(db.String(15), unique=True)  # ip address of hub on VPN tunnel
