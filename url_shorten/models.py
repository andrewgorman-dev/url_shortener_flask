from enum import unique
from url_shorten import db


class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String(20))
    long = db.Column('long', db.String(256))
    short = db.Column('short', db.String(7), unique=True)
    created_at = db.Column('created_at', db.DateTime)
    expiry_date_time = db.Column('expiry_date_time', db.DateTime)
    
    def __init__(self, name, long, short, expiry_date_time, created_at):
        self.name = name
        self.long = long
        self.short = short
        self.expiry_date_time = expiry_date_time
        self.created_at = created_at
    
    