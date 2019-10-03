from flask import Flask
from werkzeug.security import generate_password_hash
from .database import DatabaseConnection
from .base_models import BaseModels

class UserModel(BaseModels):
    def __init__(self):
        super().__init__('user')


    def register_student(self, student):
        """Function that registers a student in the user table"""
        
        query = """INSERT INTO users (username,password)\
        VALUES ('{}','{}');""".format(student['student_name'], generate_password_hash(student['student_id']))
        DatabaseConnection().save_incoming_data_or_updates(query)
    
    
    def register_university(self, university):
        """Function that registers a university in the users table"""
        
        query = """INSERT INTO users (username,password)\
        VALUES ('{}','{}');""".format(university['student_name'], generate_password_hash(university['password']))
        DatabaseConnection().save_incoming_data_or_updates(query)


    # def create_student(self, user):
    #     student = {
    #         'student_index' : user['student_index'],
    #         'firstname' : user['firstname'],
    #         'lastname' : user['lastname'],
    #         'othername' : user['othername'],
    #         'registered_on': user['registered_on']
    #     }
    #     student['username'] = [student['lastname'] + ' ' + student['firstname'] + ' '+ student['othername']]
    #     response = self.save(student)
    #     return response
    
    
    # def create_university(self, user):
    #     university = {
    #         'university_index' : user['university_index'],
    #         'university_name' : user['university_name']
    #     }
    #     response = self.save(university)
    #     return response
    