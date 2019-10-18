# third party imports
from flask import Flask, jsonify, request, abort, make_response, render_template

# local imports
from ...v1 import v1
from ..models.universities_models import UniversityModel
from ..models.users_models import UserModel
from ..schemas.schemas import UniversitiesSchema


@v1.route('/universities/all', methods=['GET'])
def get_all_universities():
    '''Gets all universities'''
    response = UniversityModel().return_data()
    return jsonify({'status' : 200,'data' : response}),200


@v1.route('/universities/<int:uni_id>', methods=['GET'])
def get_specific_university(uni_id):
    '''Checks if the university exists'''
    if not UniversityModel().check_exists("uni_id",uni_id):
        abort(make_response(jsonify({'status' : 404,'message' : 'University not found'}),404))
        
    '''If the uni_id exists it is then returned''' 
    response = UniversityModel().find('uni_id',uni_id)
    return jsonify({'status' : 200,'data' : response}),200

    
@v1.route('/universities/new', methods=['POST'])
def register_university():
    """ Endpoint that registers a new university"""
    render_template('uni_signup.html')
    json_data = request.get_json()
    
    """ Checks if there's data and if it's in json format"""
    if not json_data:
        abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))
        
    """ Checks that all the required fields have input"""
    data, errors = UniversitiesSchema().load(json_data)
    if errors:
        abort(make_response(jsonify({'status': 400, 'message': 'Empty. Please fill in all required fields', 'errors': errors}), 400))

    """ Creates the university and returns feedback in json format"""
    UniversityModel().create_university(data)
    
    """ Registers the university as a user"""
    UserModel().register_university(json_data)
    
    result = UniversityModel().find("uni_id",data['uni_id'])
    if not result:
        abort(make_response(jsonify({'status': 500, 'message': 'Unsuccessful entry'}), 500))
    else:
        return jsonify({'status': 201, 'message': 'University registered successfully', 'data': result}), 201
    


@v1.route('/universities/<int:uni_id>', methods=['DELETE'])
def delete_university(uni_id):
    '''Checks if the university exists'''
    if not UniversityModel().check_exists("uni_id",uni_id):
        abort(make_response(jsonify({'status' : 404,'message' : 'University not found'}),404))
        
    '''If the university exists it is then deleted and feedback returned ''' 
    UniversityModel().delete('uni_id',uni_id)
    if not UniversityModel().check_exists("uni_id",uni_id):
        return jsonify({'status' : 200,'message' : 'Successfully deleted'}),200
    
    
    
@v1.route('/')
def home():
    return render_template('uni_signup.html')
