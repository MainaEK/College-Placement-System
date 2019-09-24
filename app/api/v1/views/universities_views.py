# third party imports
from flask import Flask, jsonify, request, abort, make_response

# local imports
from ...v1 import v1
from ..models.universities_models import UniversityModel
from ..models.users_models import UserModel
from ..schemas.schemas import UniversitiesSchema


@v1.route('/universities/all', methods=['GET'])
def get_all_universities():
    '''Gets all universities'''
    response = UniversityModel().get_all()
    return jsonify({'status' : 200,'data' : response}),200


@v1.route('/universities/<int:university_index>', methods=['GET'])
def get_specific_university(university_index):
    '''Checks if the university exists'''
    if not UniversityModel().check_exists("university_index",university_index):
        abort(make_response(jsonify({'status' : 404,'message' : 'University not found'}),404))
        
    '''If the university_index exists it is then returned''' 
    response = UniversityModel().find('university_index',university_index)
    return jsonify({'status' : 200,'data' : response}),200

    
@v1.route('/universities/new', methods=['POST'])
def register_university():
    """ Endpoint that registers a new university"""
    json_data = request.get_json()
    
    """ Checks if there's data and if it's in json format"""
    if not json_data:
        abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))
        
    """ Checks that all the required fields have input"""
    data, errors = UniversitiesSchema().load(json_data)
    if errors:
        abort(make_response(jsonify({'status': 400, 'message': 'Empty. Please fill in all required fields', 'errors': errors}), 400))

    """ Creates the university and returns feedback in json format"""
    result = UniversityModel().register_university(json_data)
    
    """ Registers the university as a user"""
    UserModel().create_university(json_data)
    
    return jsonify({'status': 201, 'message': 'University registered successfully', 'data': result}), 201


@v1.route('/universities/<int:university_index>', methods=['DELETE'])
def delete_university(university_index):
    '''Checks if the university exists'''
    if not UniversityModel().check_exists("university_index",university_index):
        abort(make_response(jsonify({'status' : 404,'message' : 'University not found'}),404))
        
    '''If the university exists it is then deleted and feedback returned ''' 
    UniversityModel().delete('university_index',university_index)
    if not UniversityModel().check_exists("university_index",university_index):
        return jsonify({'status' : 200,'message' : 'Successfully deleted'}),200
