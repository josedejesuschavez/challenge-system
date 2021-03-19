import uuid
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from flask_jwt_extended import create_access_token

blueprint = Blueprint('log_in', __name__)

@blueprint.route('/login', methods=['GET'])
@cross_origin()
def login():
    access_token = create_access_token(identity="chavezjal")
    return jsonify(access_token=access_token)
