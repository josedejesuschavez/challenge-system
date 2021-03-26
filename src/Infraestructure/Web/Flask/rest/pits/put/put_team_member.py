import uuid
from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required

from src.Application.Service.Pits.update_team_member import UpdateTeamMember
from src.Domain.Pits.team_member import TeamMember
from src.Infraestructure.Domain.Pits.elasticsearch_team_member_repository import ElasticSearchTeamMemberRepository

blueprint = Blueprint('put_teammember', __name__)

@blueprint.route('/teammember', methods=['PUT'])
@cross_origin()
@jwt_required()
def put_team_member():
    data = request.get_json()
    id = data['id']
    team_member = TeamMember(
        active_mt=data['active_mt'],
        current_team=data['current_team'],
        date_start_team=data['date_start_team'],
        available_ops=data['available_ops'],
        email=data['email'],
        english=data['english'],
        full_name=data['full_name'],
        link_cv=data['link_cv'],
        location=data['location'],
        main_1=data['main_1'],
        main_1_score=data['main_1_score'],
        main_2=data['main_2'],
        main_2_score=data['main_2_score'],
        next_team=data['next_team'],
        next_tech_secondary=data['next_tech_secondary'],
        notes=data['notes'],
        role=data['role'],
        secondary_1=data['secondary_1'],
        secondary_1_score=data['secondary_1_score'],
        secondary_2=data['secondary_2'],
        secondary_2_score=data['secondary_2_score'],
        secondary_3=data['secondary_3'],
        secondary_3_score=data['secondary_3_score'],
        target_tech_main=data['target_tech_main'],
        techSkill=data['techSkill'],
    )
    application_service = UpdateTeamMember(id=id,
                                           team_member=team_member,
                                           repository=ElasticSearchTeamMemberRepository())
    application_service.execute()
    return jsonify({'team_members': '1'})