from src.Domain.Pits.team_member_repository import TeamMemberRepository


class GetTeamMembers(object):
    def __init__(self, repository: TeamMemberRepository):
        self.repository = repository

    def execute(self):
        team_members = self.repository.get_all()
        return team_members