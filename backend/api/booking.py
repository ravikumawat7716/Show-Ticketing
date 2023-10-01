from flask_restful import Resource
from flask import request , jsonify
from application.models import Booking , Show , Venue , Rating
from instances.database import db
from instances.api import api
from flask_jwt_extended import jwt_required , get_jwt_identity
from utils.role_required import role_required
from utils.tasks import send_mail_task
from instances.caches import cache

class BookingAPI(Resource):
    @jwt_required()
    @role_required('USER')
    def post(self):
        data = request.get_json()
        user_email = get_jwt_identity()
        booking = Booking(
            Tickets= data.get('tickets'),
            show_id = data.get('show_id'),
            user_id= user_email
        )
        db.session.add(booking)
        id = data.get('show_id')
        show = Show.query.get(id)
        if show:
            show.bookings = show.bookings + data.get('tickets')
            db.session.commit()
            cache.delete("showcache")
            showname = show.Show_Name
            bodymsg = "You have booked "+ str(data.get('tickets'))+" Tickets of " + showname+"."
            send_mail_task.delay(receiver_email = user_email, subject= "Booking Successful" , body=bodymsg)
            return {"message" : "Booked Successfully."}, 200
        else:
            return {"message" : "Invalid Show_id"} , 404

    @jwt_required()  
    def get(self):
        id = get_jwt_identity()
        alldata = []
        bookings = Booking.query.filter_by(user_id =id)
        for booking in bookings:
            id = booking.id
            showid = booking.show_id
            show = Show.query.filter_by(id = showid).first()
            venueid = show.Venue_id
            venue = Venue.query.filter_by(id = venueid).first()
            venuename = venue.Venue_Name
            showname = show.Show_Name
            timing = show.Timing
            ratings = Rating.query.filter_by(booking_id = id).first()
            if ratings:
                stars = ratings.stars
            else:
                stars = 0
            data = {
                "id" : id,
                "venuename" : venuename,
                "showname" : showname,
                "timing" : timing,
                "rating" : stars
            }
            alldata.append(data)
        if len(alldata) > 0:
            return {'bookings': alldata , "message" : "ok"} , 200
        else:
            return {"message" : "Bookings Not Found"} , 200




    
api.add_resource(BookingAPI, '/book')

