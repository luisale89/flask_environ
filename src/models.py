from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__="user"
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    fname = db.Column(db.String(150), nullable=False)
    lname = db.Column(db.String(150), nullable=False)
    rut = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return "<User %r>" % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "fname": self.fname,
            "lname": self.lname
        }

    
