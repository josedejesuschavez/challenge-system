from src.Domain.Pits.team_member import TeamMember
from src.Domain.Pits.team_member_repository import TeamMemberRepository


class UpdateTeamMember(object):
    def __init__(self, id, team_member: TeamMember, repository: TeamMemberRepository):
        self.id = id
        self.team_member = team_member
        self.repository = repository

    def execute(self):
        self.repository.update(self.id, self.team_member)