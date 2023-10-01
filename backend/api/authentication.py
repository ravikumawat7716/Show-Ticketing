from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from instances.api import api
from flask_restful import Resource
from flask import request
from instances.database import db
from application.models import User, Role
from datetime import timedelta
# from utils.mail.mail import send_mail
from utils.tasks import send_mail_task





class RegistrationAPI(Resource):
    def post(self):
        data = request.get_json()
        print("processing the request")
        if data.get('name') and data.get('email') and data.get('password'):
            if User.query.filter_by(email=data['email']).first():
                return {'message': 'User already exists'}, 409
            else:
                user = User(
                    name = data['name'],
                    email = data['email'],
                    password=generate_password_hash(data['password']),
                    role="USER"
                )
                db.session.add(user)
                db.session.commit()
                bodymsg = "Hi "+data['name']+"\n"+"You're Successfully Registered. Your username is: "+data['email']+" and password is : "+data['password']+" You can login here: https://13.235.83.235/login"
                #send_mail(receiver_email = user.email, subject= "Registration Successful" , body=bodymsg)
                send_mail_task.delay(receiver_email = user.email, subject= "Registration Successful" , body=bodymsg)
                print("sending the response")
                return {'message': 'User Registration Successful. You can login now.'} ,201
            
    
class UserLoginAPI(Resource):
    def post(self):
        data = request.get_json()
        if data.get('email') and data.get('password'):
            email = data['email']
            password=data['password']
            user_from_db = User.query.filter_by(email=email).first()
            if user_from_db and check_password_hash(user_from_db.password, password):
                access_token = create_access_token(identity=email, expires_delta=timedelta(days=2))
                name = user_from_db.name
                role = user_from_db.role
                return {'access_token': access_token , 'username' : name , 'userrole' : role}, 200
            return {'message': 'Incorrect Credentials'} , 401
        return {'message': 'Bad Request'} , 400

            

api.add_resource(RegistrationAPI, '/register')
api.add_resource(UserLoginAPI, '/login')

