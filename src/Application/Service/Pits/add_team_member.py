from src.Domain.Pits.team_member_repository import TeamMemberRepository


class AddTeamMember(object):
    def __init__(self, id, team_member, repository: TeamMemberRepository):
        self.id = id
        self.team_member = team_member
        self.repository = repository

    def execute(self):
        self.repository.add(self.id, self.team_member)