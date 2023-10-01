import os
from instances.app import app
from instances.database import db
from dotenv import load_dotenv
from utils.configuration import create_app, initialise_database
from flask import Flask, request, jsonify
from flask_jwt_extended import  jwt_required, get_jwt_identity
from instances.caches import cache
from utils.tasks import test, export_monthly_bookings, dailyreport
import api
load_dotenv()



celeryservice = create_app()
initialise_database()

@app.route("/")
def home():
    test.delay()
    # export_monthly_bookings.delay()
    # dailyreport.delay()
    return '<h1>Backend server is running.</h1> <br> <a href="http://localhost:8080/">Click here to Access the frontend.</a>'


if __name__ == '__main__':
    app.run()