from flask_restful import Resource
from flask import request
from application.models import Venue , Show , Booking
from instances.database import db
from instances.api import api
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from utils.role_required import role_required
from instances.caches import cache


class VenueAPI(Resource):
    @jwt_required()
    @role_required('ADMIN')
    def post(self):
        data = request.get_json()
        if data.get('Venue_Name') and data.get('Place') and data.get('Location') and data.get('Capacity'):
            if Venue.query.filter_by(Venue_Name=data.get('Venue_Name')).first():
                return {'message': 'Venue already exists'}, 409
            else:
                venue = Venue(
                    Venue_Name=data.get('Venue_Name'),
                    Place=data.get('Place'),
                    Location=data.get('Location'),
                    Capacity=data.get('Capacity')
                )
                db.session.add(venue)
                db.session.commit()
                cache.delete('venuecache')
                return {'message': 'Venue Created Successfully'} , 201
        return {'message': 'Something went wrong. Missing required fields.'}, 400

    @jwt_required()
    def put(self):
        data = request.get_json()
        if data.get('id') and data.get('Venue_Name') and data.get('Place') and data.get('Location') and data.get('Capacity'):
            venue = Venue.query.get(data.get('id'))
            if venue:
                old_capacity = venue.Capacity
                venue.Venue_Name = data.get('Venue_Name')
                venue.Place = data.get('Place')
                venue.Location = data.get('Location')
                db.session.commit()
                cache.delete('venuecache')
                venue = Venue.query.get(data.get('id'))
                if old_capacity != data.get('Capacity'):
                    associated_shows = Show.query.filter_by(Venue_id=data.get('id')).all()
                    for show in associated_shows:
                        bookings = show.bookings
                        if bookings < data.get('Capacity'):
                            return {'message': 'All the values except Capacity are updated. Capacity was not updated because we have prior bookings > capacity.'} , 200
                            break
                    for show in associated_shows:
                        show.seats = data.get('Capacity')
                        db.session.commit()
                venue.Capacity = data.get('Capacity')
                db.session.commit()
                return {'message': 'Venue updated successfully'}, 200
            else:
                return {'message': 'Venue not found'}, 404
        else:
            return {'message': 'Bad request'}, 400
        
    @jwt_required()
    @cache.cached(timeout=300 , key_prefix="venuecache")
    def get(self):
        venues = Venue.query.all()
        serialized_venues = []
        for venue in venues:
            venue_data = {
                'id': venue.id,
                'Venue_Name': venue.Venue_Name,
                'Place': venue.Place,
                'Location': venue.Location,
                'Capacity': venue.Capacity
            }
            serialized_venues.append(venue_data)

        return {'venues': serialized_venues}, 200
    
    @jwt_required()
    def delete(self):
        data = request.get_json()
        if data.get('id'):
            venue = Venue.query.get(data.get('id'))
            if venue:
                associated_shows = Show.query.filter_by(Venue_id=data.get('id')).all()
                for show in associated_shows:
                    showid = show.id
                    associated_bookings = Booking.query.filter_by(show_id = showid)
                    for booking in associated_bookings:
                        db.session.delete(booking)
                    db.session.delete(show)
                Venue.query.filter_by(id=data.get('id')).delete()
                db.session.commit()
                cache.delete('venuecache')
                cache.delete("showcache")
                return {'message': 'Venue deleted successfully'}, 200
            else:
                return {'message': 'Venue not found'}, 404
        else:
            return {'message': 'Bad request'}, 400



api.add_resource(VenueAPI, '/venue')



