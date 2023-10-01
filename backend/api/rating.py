from flask_restful import Resource
from flask_jwt_extended import jwt_required , get_jwt_identity
from application.models import Venue, Show , Rating , Booking
from flask import request, jsonify
from instances.api import api
from instances.database import db
from utils.role_required import role_required
from instances.caches import cache

class RatingAPI(Resource):
    @jwt_required()
    @role_required('USER')
    def post(self):
       data = request.get_json()
       user_email = get_jwt_identity()
       booking = Booking.query.filter_by(id = data.get('booking_id')).first()
       show_id = booking.show_id
       show = Show.query.filter_by(id = show_id).first()
       venue_id = show.Venue_id
       rating = Rating(
            stars= data.get('stars'),
            booking_id = data.get('booking_id'),
            user_id= user_email,
            show_id = show_id,
            venue_id = venue_id
        )
       db.session.add(rating)
       db.session.commit()
       cache.delete("showcache")
       
       return {"message" : "Rating Submitted Successfully."}, 200
    

api.add_resource(RatingAPI, '/rate')