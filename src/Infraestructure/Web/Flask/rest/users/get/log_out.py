import uuid
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin


blueprint = Blueprint('log_out', __name__)

@blueprint.route('/logout', methods=['GET'])
@cross_origin()
def login():
    return jsonify({'token_id': '-134'})