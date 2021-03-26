import json
from datetime import datetime

from elasticsearch import Elasticsearch

from src.Domain.Pits.team_member import TeamMember
from src.Domain.Pits.team_member_repository import TeamMemberRepository


class ElasticSearchTeamMemberRepository(TeamMemberRepository):

    def __init__(self):
        self.es = Elasticsearch(
            hosts=[{'host': 'elasticsearch'}]
        )

    def delete_by_id(self, id):
        self.es.delete(index="pits", doc_type="_doc", id=id)

    def update(self, id, team_member):
        json_team_member = json.dumps(team_member.__dict__)
        self.es.index(index="pits", doc_type="_doc", id=id, body=json_team_member)

    def add(self, id, team_member):
        json_team_member = json.dumps(team_member.__dict__)
        self.es.index(index="pits", doc_type="_doc", id=id, body=json_team_member)

    def get_all(self):
        team_members = []
        result = self.es.search(index="pits", doc_type="_doc", body={"query": {"match_all": {}}})

        for hit in result['hits']['hits']:
            hit['_source']['id']=hit['_id']
            team_member=hit['_source']
            team_members.append(team_member)

        return team_members