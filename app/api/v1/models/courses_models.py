from flask import Flask
from .database import DatabaseConnection
from .base_models import BaseModels


class CourseModel(BaseModels):
    def __init__(self):
        super().__init__('courses')
        

    def create_course(self, course):
        """Function that creates a course in the courses table"""
        
        query = """INSERT INTO courses (course_id,course_name,uni_id,requirements)\
        VALUES ('{}','{}','{}','{}');""".format(course['course_id'], course['course_name'], course['uni_id'], course['requirements'])
        DatabaseConnection().save_incoming_data_or_updates(query)
        
        # query = """SELECT * FROM courses WHERE course_id = {};""".format(course['course_id'])
        # result = DatabaseConnection().fetch_single_data_row(query)
        # return result
    
    
    
    # def register_course(self, courses):
    #     courses = {
    #         'courses_id' : courses['courses_id'],
    #         'courses_name' : courses['courses_name'],
    #         'uni_id' : courses['uni_id'],
    #         'requirements' : courses['requirements']
    #     }
    #     response = self.save(courses)
    #     return response
    