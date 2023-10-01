from instances.database import db
from datetime import datetime , date

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(255))
    role = db.Column(db.String(80), db.ForeignKey('role.name'))

# Role model
class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(300))

#Venue
class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Venue_Name= db.Column(db.String(100), unique=True )
    Place = db.Column(db.String(100))
    Location = db.Column(db.String(100))
    Capacity = db.Column(db.Integer)

#Show
class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Show_Name= db.Column(db.String(200))
    seats = db.Column(db.Integer)
    bookings = db.Column(db.Integer)
    Rating = db.Column(db.String(100))
    Timing = db.Column(db.String(100))
    Tags = db.Column(db.String(300))
    Price = db.Column(db.Integer)
    Venue_id = db.Column(db.String(80),db.ForeignKey('venue.id'), nullable=False)

#Bookings
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Tickets= db.Column(db.Integer)
    show_id = db.Column(db.Integer,db.ForeignKey('show.id'),nullable=False )
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    booking_date = db.Column(db.Date, default=date.today)
    
    
    
#Ratings
class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Integer)
    booking_id= db.Column(db.Integer)
    show_id = db.Column(db.Integer,db.ForeignKey('show.id'),nullable=False )
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)