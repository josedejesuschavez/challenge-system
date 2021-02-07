import uuid
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin


blueprint = Blueprint('users', __name__)

@blueprint.route('/login', methods=['GET'])
@cross_origin()
def login():
    return jsonify({'token_id': '-134'})