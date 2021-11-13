import os
class BaseConfig():
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')
    user = "root"
    password="123456"
    dbName="flaskDB"
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False  
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_DATABASE_URI = "mysql://{user}:{password}@127.0.0.1:3306/{db}".format(user=user,password=password,db=dbName)