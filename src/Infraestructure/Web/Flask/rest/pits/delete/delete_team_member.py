from flask import Blueprint, jsonify
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required

from src.Application.Service.Pits.delete_team_member import DeleteTeamMember
from src.Infraestructure.Domain.Pits.elasticsearch_team_member_repository import ElasticSearchTeamMemberRepository

blueprint = Blueprint('delete_teammember', __name__)

@blueprint.route('/teammember/<id>', methods=['DELETE'])
@cross_origin()
@jwt_required()
def delete_team_member(id):
    application_service = DeleteTeamMember(id, repository=ElasticSearchTeamMemberRepository())
    application_service.execute()
    return jsonify({'team_members': id})