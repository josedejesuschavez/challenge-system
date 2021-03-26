from flask import Blueprint, jsonify
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required

from src.Application.Service.Pits.get_team_members import GetTeamMembers
from src.Infraestructure.Domain.Pits.elasticsearch_team_member_repository import ElasticSearchTeamMemberRepository

blueprint = Blueprint('get_teammembers', __name__)

@blueprint.route('/teammembers', methods=['GET'])
@cross_origin()
@jwt_required()
def get_team_members():
    application_service = GetTeamMembers(repository=ElasticSearchTeamMemberRepository())
    team_members = application_service.execute()
    return jsonify({'team_members': team_members})
