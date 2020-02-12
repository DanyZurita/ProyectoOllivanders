import os
from flask_sqlalchemy import SQLAlchemy
from app import app


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class GildedRose(db.Model):
    __tablename__ = 'gildedrose'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    sellin = db.Column(db.Integer(3))
    quality = db.Column(db.Integer(3))

    def __repr__(self):
        return '<Stock: %r>' % (self.name, self.sellin, self.quality)
