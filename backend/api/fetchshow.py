from flask_restful import Resource
from flask_jwt_extended import jwt_required
from application.models import Venue, Show
from flask import request, jsonify
from instances.api import api

class ShowFetchAPI(Resource):
    @jwt_required()
    def get(self):
        id = request.args.get('id')
        if id is not None:
            show = Show.query.filter_by(id=id).first()
            if show:
                if show.seats is not None and show.bookings is not None:
                    showseats = show.seats - show.bookings
                venue_id = show.Venue_id
                venue = Venue.query.filter_by(id=venue_id).first()
                showname = show.Show_Name
                venuename = venue.Venue_Name
                seats = showseats
                price = show.Price
                timing = show.Timing
                showdata = {
                            "showname" : showname,
                            "venuename" : venuename,
                            "seats" : seats,
                            "price" : price,
                            "timing" : timing
                        }
                return jsonify(showdata)
            else:
                return jsonify({'message': 'Show not found'}), 404
        else:
            return jsonify({'message': 'Missing or invalid id parameter'}), 400

api.add_resource(ShowFetchAPI, '/fetch_showdata')