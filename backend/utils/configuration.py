from werkzeug.security import generate_password_hash
from instances.app import app
from instances.database import db
from instances.api import api
from application.config import Config
from application.models import User , Role
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from instances.mail import mail
from instances.caches import cache
from instances.celery import celeryservice


def create_app():
    app.config.from_object(Config)
    
    celeryservice.conf.broker_url = app.config["CELERY_BROKER_URL"]
    celeryservice.conf.result_backend = app.config["CELERY_RESULT_BACKEND"]
    celeryservice.conf.enable_utc = app.config["ENABLE_UTC"]
    celeryservice.conf.timezone = app.config["TIMEZONE"]
    class ContextTask(celeryservice.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celeryservice.Task = ContextTask

    db.init_app(app)
    api.init_app(app)
    CORS(app)
    JWTManager(app)
    mail.init_app(app)
    cache.init_app(app)

    app.app_context().push()
    
    print("returning celery service")
    return celeryservice
    

def initialise_database():
   with app.app_context():
        from instances.caches import cache
        inspector = db.inspect(db.engine)
        table_names = inspector.get_table_names()

        if not table_names:  # If no tables exist
            db.create_all()
            print("Database created sucessfully")
            User_role = Role(name='USER', description='User can book tickets, Add Testimonials.')
            Admin_role = Role(name='ADMIN', description='ADMIN can create new venues ,  create new shows , approve testimonials.')
            Admin_Email = input("Enter Admin Email Address :  ")
            Admin_Password = input("Create a password for Admin :  ")
            Admin_Password = generate_password_hash(Admin_Password)

            Admin_Profile = User (
                name = 'Admin',
                email = Admin_Email,
                password = Admin_Password,
                role = "ADMIN"
                )
                
                
            db.session.add(User_role)
            db.session.add(Admin_role)
            db.session.add(Admin_Profile)
            db.session.commit()
            print("Admin Profile Created Sucessfully.")
        else:
            print("Database already exists")

    