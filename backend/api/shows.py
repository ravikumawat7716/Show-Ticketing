from flask_restful import Resource
from flask import request
from application.models import Show , Venue , Booking , Rating
from instances.database import db
from instances.api import api
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from utils.role_required import role_required
from instances.caches import cache


class ShowAPI(Resource):
    @jwt_required()
    @role_required('ADMIN')
    def post(self):
        data = request.get_json()
        if data.get('Show_Name') and data.get('Rating') and data.get('Timing') and data.get('Tags') and data.get('Price') and data.get('Venue_id'):
            if Show.query.filter_by(Show_Name=data.get('Show_Name'), Venue_id=data.get('Venue_id')).first():
                return {'message': 'Show already exists'}, 409
            else:
                venue = Venue.query.filter_by(id = data.get('Venue_id')).first()
                if venue:
                    show = Show(
                        Show_Name=data.get('Show_Name'),
                        Rating=data.get('Rating'),
                        Timing=data.get('Timing'),
                        Tags=data.get('Tags'),
                        Price = data.get('Price'),
                        Venue_id = data.get('Venue_id'),
                        seats = venue.Capacity,
                        bookings = 0
                    )
                db.session.add(show)
                db.session.commit()
                cache.delete("showcache")
                return {'message': 'Show Created Successfully'} , 201
        return {'message': 'Something went wrong. Missing required fields.'}, 400
    
    @jwt_required()
    @role_required('ADMIN')
    def put(self):
        data = request.get_json()
        if data.get('Show_Name') and data.get('Rating') and data.get('Timing') and data.get('Tags') and data.get('Price') and data.get('id'):
            id=data.get('id')
            show = Show.query.get(id)
            if show:
                show.Show_Name=data.get('Show_Name')
                show.Rating=data.get('Rating')
                show.Timing=data.get('Timing')
                show.Tags=data.get('Tags')
                show.Price = data.get('Price')
                db.session.commit()
                cache.delete("showcache")
                return {'message' : "updated successfully"} , 200
            else:
                return {'message' : "show not found."} , 400
        else:
            return {"message" : "something went wrong"} , 400
        
    @jwt_required()    
    @cache.cached(timeout=300, key_prefix="showcache")  
    def get(self):
        shows = Show.query.all()
        serialized_shows = []
        for show in shows:
            if show.seats is not None and show.bookings is not None:
                show.seats = show.seats - show.bookings
                showratings = Rating.query.filter_by(show_id = show.id).all()
                if len(showratings) > 0:
                    sum = 0
                    count = 0
                    for showrating in showratings:
                        sum = sum + showrating.stars
                        count = count + 1
                    avg_stars = float(sum)/float(count)
                    adminrating = float(show.Rating)
                    rating = (0.5*(adminrating))+(0.5*(avg_stars))
                else:
                    rating = float(show.Rating)

            formatted_rating = "{:.1f}".format(rating)
            show_data = {
                'id': show.id,
                'Show_Name': show.Show_Name,
                'Rating': formatted_rating,
                'Timing': show.Timing,
                'Available_Seats': show.seats,
                'Venue_id': show.Venue_id,
                'Tags': show.Tags,
                'Price': show.Price
            }
            serialized_shows.append(show_data)

        return {'shows': serialized_shows}, 200
    
    @jwt_required()
    @role_required('ADMIN')
    def delete(self):
        data = request.get_json()
        show_id = data.get('id')
        existing_show = Show.query.filter_by(id = show_id).first()
        if existing_show:
            Show.query.filter_by(id = show_id).delete()
            associated_bookings = Booking.query.filter_by(show_id = show_id)
            for booking in associated_bookings:
                db.session.delete(booking)
            db.session.commit()
            cache.delete("showcache")
            return {'message' : 'Show deleted sucessfully'} , 200
        else:
            return {'message' : 'bad request'}, 400


api.add_resource(ShowAPI, '/show')




