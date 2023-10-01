import os 
from datetime import datetime, timedelta
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(".env")

if os.getenv("SECRET_KEY"):
    print("Environment Variables Fetched Successfully")
else:
    print("Something is wrong with Enviroment Variables.")


# configuration 
class Config():
    DEBUG = True 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    JWT_SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=2)
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')
    ENABLE_UTC = os.getenv('ENABLE_UTC')
    TIMEZONE = os.getenv('TIMEZONE')
    CACHE_TYPE = "redis"
    CACHE_REDIS_URL = os.getenv("CACHE_REDIS_URL")
    # CACHE_TYPE = "simple"
    



    
    


