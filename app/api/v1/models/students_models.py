from flask import Flask
from .database import DatabaseConnection
from .base_models import BaseModels


class StudentModel(BaseModels):
    def __init__(self):
        super().__init__('students')
        
    def create_student(self, student):
        """Function that creates a student in the students table"""
        
        query = """INSERT INTO students (student_id,student_name,grades,course_id)\
        VALUES ('{}','{}','{}','{}');""".format(student['student_id'], student['student_name'], student['grades'], student['course_id'])
        DatabaseConnection().save_incoming_data_or_updates(query)



    # def register_student(self, student):
    #     student = {
    #         'student_index' : student['student_index'],
    #         'student_name' : student['student_name'],
    #         'student_id' : student['student_id'],
    #         'grades' : student['grades']
    #     }
    #     response = self.save(student)
    #     return response
    