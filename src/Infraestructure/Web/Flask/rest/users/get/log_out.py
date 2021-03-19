import uuid
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required

blueprint = Blueprint('log_out', __name__)

@blueprint.route('/logout', methods=['GET'])
@cross_origin()
@jwt_required()
def login():
    return jsonify({'token_id': 'logout'})