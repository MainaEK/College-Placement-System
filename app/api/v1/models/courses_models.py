from datetime import datetime

from .base_models import BaseModels


class CourseModel(BaseModels):
    def __init__(self):
        super().__init__('courses')
        
        
    def get_all(self):
        # self.db = BaseModels(db = 'courses')
        response = self.db.return_data()
        return response



    def register_course(self, courses):
        courses = {
            'courses_id' : courses['courses_id'],
            'courses_name' : courses['courses_name'],
            'uni_id' : courses['uni_id'],
            'requirements' : courses['requirements']
        }
        response = self.save(courses)
        return response
    