import uuid
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

from src.Application.Service.Authentication.authenticate_user import AuthenticateUser
from src.Infraestructure.Domain.Users.sqlalchemy_token_repository import SQLAlchemyTokenRepository
from src.Infraestructure.Domain.Users.sqlalchemy_user_repository import SQLAlchemyUserRepository

blueprint = Blueprint('log_in', __name__)

@blueprint.route('/login', methods=['POST'])
@cross_origin()
def login():
    try:
        data = request.get_json()
        application_service = AuthenticateUser(email=data['email'],
                                               password=data['password'],
                                               user_repository=SQLAlchemyUserRepository(),
                                               token_repository=SQLAlchemyTokenRepository())
        token=application_service.execute()
        return jsonify({'token': token})
    except Exception as exception:
        return jsonify({'token': '-1', 'error': str(exception)})