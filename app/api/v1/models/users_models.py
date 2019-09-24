from datetime import datetime

from .base_models import BaseModels

class UserModel(BaseModels):
    def __init__(self):
        super().__init__('user')

    def create_student(self, user):
        student = {
            'student_index' : user['student_index'],
            'firstname' : user['firstname'],
            'lastname' : user['lastname'],
            'othername' : user['othername'],
            'registered_on': user['registered_on']
        }
        student['username'] = [student['lastname'] + ' ' + student['firstname'] + ' '+ student['othername']]
        response = self.save(student)
        return response
    
    
    def create_university(self, user):
        university = {
            'university_index' : user['university_index'],
            'university_name' : user['university_name']
        }
        response = self.save(university)
        return response
    