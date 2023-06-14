from . import db


class Modules(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(15), unique=True)  # Local ip of module
    name = db.Column(db.String(100), unique=True)
