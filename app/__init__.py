'''Creating app'''
import os
from flask import Flask
# from dotenv import load_dotenv
from instance.config import app_config
from app.api.v1.views.students_views import v1 as students_blueprint
from app.api.v1.models.database import DatabaseConnection 
from app.api.v1.models.db_tables import create_admin 

"""importing the configurations from the .config file which is in the instance folder"""
def create_app(config_name):
    '''creating  the app using the configurations in the dictionary created in the .config file'''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.register_blueprint(students_blueprint)
    
    # load_dotenv()
    # db_url = os.environ.get('DATABASE_URL')
    try:
        DatabaseConnection().drop_all_tables()
        DatabaseConnection().create_tables_and_admin()
        print("Database successfully connected")
        
    except Exception:
        print("Unable to make db connection")
    
    
    return app
