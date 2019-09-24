# third party imports
from flask import Flask, jsonify, request, abort, make_response

# local imports
from ...v1 import v1
from ..models.students_models import StudentModel
from ..models.users_models import UserModel
from ..schemas.schemas import StudentSchema


@v1.route('/students/all/', methods=['GET'])
def get_all_students():
    '''Gets all students'''
    response = StudentModel().get_all()
    return jsonify({'status' : 200,'data' : response}),200


@v1.route('/students/<int:student_index>/', methods=['GET'])
def get_specific_student(student_index):
    '''Checks if the student exists'''
    if not StudentModel().check_exists("student_index",student_index):
        abort(make_response(jsonify({'status' : 404,'message' : 'Student not found'}),404))
        
    '''If the student_index exists it is then returned''' 
    response = StudentModel().find('student_index',student_index)
    return jsonify({'status' : 200,'data' : response}),200

    
@v1.route('/students/new/', methods=['POST'])
def register_student():
    """ Endpoint that registers a new student"""
    json_data = request.get_json()
    
    """ Checks if there's data and if it's in json format"""
    if not json_data:
        abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))
        
    """ Checks that all the required fields have input"""
    data, errors = StudentSchema().load(json_data)
    if errors:
        abort(make_response(jsonify({'status': 400, 'message': 'Empty. Please fill in all required fields', 'errors': errors}), 400))

    """ Creates the student and returns feedback in json format"""
    result = StudentModel().register_student(data)
    
    """ Registers the university as a user"""
    UserModel().create_student(json_data)
    
    return jsonify({'status': 201, 'message': 'Student registered successfully', 'data': result}), 201


@v1.route('/students/<int:student_index>/', methods=['DELETE'])
def delete_student(student_index):
    '''Checks if the student exists'''
    if not StudentModel().check_exists("student_index",student_index):
        abort(make_response(jsonify({'status' : 404,'message' : 'Student not found'}),404))
        
    '''If the student exists it is then deleted and feedback returned ''' 
    StudentModel().delete('student_index',student_index)
    if not StudentModel().check_exists("student_index",student_index):
        return jsonify({'status' : 200,'message' : 'Successfully deleted'}),200
