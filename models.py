from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def setup_db(app):
    app.config.from_object('config')
    db.app = app
    db.init_app(app)
    Migrate(app, db)
    return db

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    address = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)
    genres = db.Column(db.String(120), nullable=True)
    image_link = db.Column(db.String(500), nullable=True)    
    website_link = db.Column(db.String(500), nullable=True)    
    facebook_link = db.Column(db.String(500), nullable=True)
    seeking_talent = db.Column(db.Boolean, nullable=True)
    seeking_description = db.Column(db.String(500), nullable=True)
    date_added = db.Column(db.DateTime, nullable=True)

    venue_shows = db.relationship('Show', back_populates='venue', lazy=True)       

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    city = db.Column(db.String(120), nullable=True)
    state = db.Column(db.String(2), nullable=True)
    phone = db.Column(db.String(120), unique=True, nullable=False)
    genres = db.Column(db.String(120), nullable=True)
    image_link = db.Column(db.String(500), nullable=True)
    website_link = db.Column(db.String(500), nullable=True)
    facebook_link = db.Column(db.String(500), nullable=True)
    seeking_venue = db.Column(db.Boolean, nullable=True)
    seeking_description = db.Column(db.String(500), nullable=True) 
    date_added = db.Column(db.DateTime, nullable=False)
    available_hours = db.Column(db.String(5), nullable=True)

    artist_shows = db.relationship('Show', back_populates='artist', lazy=True)

class Show(db.Model):
  __tablename__ = 'Show'
  
  id = db.Column(db.Integer, primary_key=True)
  venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)
  artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)
  
  start_time = db.Column(db.DateTime, nullable=False)

  venue = db.relationship('Venue', back_populates='venue_shows')
  artist = db.relationship('Artist', back_populates='artist_shows')