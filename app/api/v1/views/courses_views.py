# third party imports
from flask import Flask, jsonify, request, abort, make_response

# local imports
from ...v1 import v1
from ..models.courses_models import CourseModel
from ..schemas.schemas import CourseSchema


@v1.route('/courses/all', methods=['GET'])
def get_all_courses():
    '''Gets all courses'''
    response = CourseModel().get_all()
    return jsonify({'status' : 200,'data' : response}),200


@v1.route('/courses/<int:course_index>', methods=['GET'])
def get_specific_course(course_index):
    '''Checks if the course exists'''
    if not CourseModel().check_exists("course_index",course_index):
        abort(make_response(jsonify({'status' : 404,'message' : 'Course not found'}),404))
        
    '''If the course_index exists it is then returned''' 
    response = CourseModel().find('course_index',course_index)
    return jsonify({'status' : 200,'data' : response}),200

    
@v1.route('/courses/new', methods=['POST'])
def register_course():
    
    """ Endpoint that registers a new course"""
    json_data = request.get_json()
    
    """ Checks if there's data and if it's in json format"""
    if not json_data:
        abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))
        
    """ Checks that all the required fields have input"""
    data, errors = CourseSchema().load(json_data)
    if errors:
        abort(make_response(jsonify({'status': 400, 'message': 'Empty. Please fill in all required fields', 'errors': errors}), 400))

    """ Creates the course and returns feedback in json format"""
    result = CourseModel().register_course(data)
    return jsonify({'status': 201, 'message': 'Course registered successfully', 'data': result}), 201


@v1.route('/courses/<int:course_index>', methods=['DELETE'])
def delete_course(course_index):
    '''Checks if the course exists'''
    if not CourseModel().check_exists("course_index",course_index):
        abort(make_response(jsonify({'status' : 404,'message' : 'Course not found'}),404))
        
    '''If the course exists it is then deleted and feedback returned ''' 
    CourseModel().delete('course_index',course_index)
    if not CourseModel().check_exists("course_index",course_index):
        return jsonify({'status' : 200,'message' : 'Successfully deleted'}),200
