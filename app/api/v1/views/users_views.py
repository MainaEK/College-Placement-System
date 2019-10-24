# standard imports
from flask import Flask, jsonify, request, Response, json, abort, make_response, render_template
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

# local imports
from ..models.users_models import UserModel
from ...v1 import v1

@v1.route('/auth/login', methods=['POST'])
def login():
    """ Endpoint to login a user"""
    json_data = request.get_json()

    """Checks if there's data and if it's in json format"""
    if not json_data:
        abort(make_response(
            jsonify({'status': 400, 'message': 'Sorry but the data provided should be in json'}), 400))

    """Checks if the user exists"""
    if not UserModel().check_exists("username", json_data['username']):
        abort(make_response(
            jsonify({'status': 404, 'message': 'No such user has been registered'}), 404))

    """Checks if the password is correct"""
    response = UserModel().find(json_data['username'])
    if not check_password_hash(response['password'], json_data['password']):
        abort(make_response(
            jsonify({'status': 400, 'message': 'Incorrect password'}), 400))

        """Logs in the user"""
    else:
        access_token = create_access_token(identity=response['isAdmin'])

    return jsonify({'status': 200, 'data': [{'token': access_token, 'message': 'Login Successful'}]}), 200
    
