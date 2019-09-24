"""
This contains the schemas
"""
from marshmallow import Schema, fields
from ..utils.validations import Not_null_string, password_check


class CourseSchema(Schema):
    """ Class to validate schema for course object """

    course_name = fields.Str(required=True, validate=Not_null_string)
    requirements = fields.List(fields.Str, required=True, validate=Not_null_string)
    uni_id = fields.Int(required=True, validate=Not_null_string)
    
class StudentSchema(Schema):
    """ Class to validate schema for student object """

    student_name = fields.Str(required=True, validate=Not_null_string)
    grades = fields.List(fields.Str, required=True, validate=Not_null_string)
    student_index = fields.Int(required=True, validate=Not_null_string)
    
class UniversitiesSchema(Schema):
    """ Class to validate schema for universities object """

    university_name = fields.Str(required=True, validate=Not_null_string)
    university_id = fields.Int(required=True, validate=Not_null_string)
    