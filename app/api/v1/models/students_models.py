from datetime import datetime

from .base_models import BaseModels


class StudentModel(BaseModels):
    def __init__(self):
        super().__init__('students')
        
        
    def get_all(self):
        #self.db = BaseModels(db = 'students')
        response = self.return_data()
        return response


    def register_student(self, student):
        student = {
            'student_index' : student['student_index'],
            'student_name' : student['student_name'],
            'course_id' : student['course_id'],
            'grades' : student['grades']
        }
        response = self.save(student)
        return response
    