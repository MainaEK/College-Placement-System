'''Creating app'''
import os
from flask import Flask, jsonify, render_template
from flask_jwt_extended import (JWTManager)
from instance.config import app_config
from app.api.v1.views.students_views import v1 as students_blueprint
from app.api.v1.views.courses_views import v1 as courses_blueprint
from app.api.v1.views.universities_views import v1 as universities_blueprint
from app.api.v1.views.users_views import v1 as users_blueprint
from app.api.v1.models.database import DatabaseConnection 
# from app.api.v1.models.db_tables import create_admin 

"""importing the configurations from the .config file which is in the instance folder"""
def create_app(config_name):
    '''creating  the app using the configurations in the dictionary created in the .config file'''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.register_blueprint(students_blueprint)
    app.register_blueprint(courses_blueprint)
    app.register_blueprint(universities_blueprint)
    app.register_blueprint(users_blueprint)
    
    try:
        DatabaseConnection().drop_all_tables()
        DatabaseConnection().create_tables_and_admin()
        print("Database successfully connected")
        
    except Exception:
        print("Unable to make db connection")
    
    app.config['JWT_SECRET_KEY'] = 'secret'
    jwt = JWTManager(app)
    
    @app.route('/') 
    def index():
        return render_template('index.html')

    @app.route('/university/registration')
    def unireg():
        return render_template('uni_signup.html')
    
    @app.route('/university/dashboard')
    def unidash():
        return render_template('uni_dash.html')
    
        
    @app.route('/student/dash')
    def studentdash():
        return render_template('s_dash.html')
    
    
    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify({
            'status': 404,
            'message': 'Url not found. Check your url and try again'
        }), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'status': 500,
            'message': 'Sorry but your request could not be processed'}), 500
    
    return app


