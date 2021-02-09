import uuid
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin


blueprint = Blueprint('log_in', __name__)

@blueprint.route('/login', methods=['GET'])
@cross_origin()
def login():
    return jsonify({'token_id': 'login'})
