# third party imports
from flask import Flask, jsonify, request, abort, make_response
from flask_jwt_extended import (jwt_required, get_jwt_identity)

# local imports
from ...v1 import v1
from ..models.students_models import StudentModel
from ..models.users_models import UserModel
from ..schemas.schemas import StudentSchema


@v1.route('/students/all/', methods=['GET'])
def get_all_students():
    '''Gets all students'''
    response = StudentModel().return_data()
    return jsonify({'status' : 200,'data' : response}),200


@v1.route('/students/<int:student_id>/', methods=['GET'])
def get_specific_student(student_id):
    '''Checks if the student exists'''
    if not StudentModel().check_exists("student_id",student_id):
        abort(make_response(jsonify({'status' : 404,'message' : 'Student not found'}),404))
        
    '''If the student_id exists it is then returned''' 
    response = StudentModel().find('student_id',student_id)
    return jsonify({'status' : 200,'data' : response}),200

    
@v1.route('/students/new/', methods=['POST'])
@jwt_required
def register_student():
    """Checks to see if the user is the admin"""
    isAdmin = get_jwt_identity()
    if not isAdmin == 'True':
        abort(make_response(
                jsonify({'status': 401, 'message': 'Unauthorized for current user'}), 401))
        
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
    StudentModel().create_student(data)
    
    """ Registers the university as a user"""
    UserModel().register_student(data)
    
    result = StudentModel().find("student_id",data['student_id'])
    if not result:
        abort(make_response(jsonify({'status': 500, 'message': 'Unsuccessful entry'}), 500))
    else:
        return jsonify({'status': 201, 'message': 'Student registered successfully', 'data': result}), 201


@v1.route('/students/<int:student_id>/', methods=['DELETE'])
def delete_student(student_id):
    '''Checks if the student exists'''
    if not StudentModel().check_exists("student_id",student_id):
        abort(make_response(jsonify({'status' : 404,'message' : 'Student not found'}),404))
        
    '''If the student exists it is then deleted and feedback returned ''' 
    StudentModel().delete('student_id',student_id)
    if not StudentModel().check_exists("student_id",student_id):
        return jsonify({'status' : 200,'message' : 'Successfully deleted'}),200
