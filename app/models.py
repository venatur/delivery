from . import db


class User(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    company = db.Column(db.String(32))
    password_hash = db.Column(db.String(128))