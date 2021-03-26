from src.Domain.Pits.team_member_repository import TeamMemberRepository


class DeleteTeamMember(object):

    def __init__(self, id, repository: TeamMemberRepository):
        self.id = id
        self.repository = repository

    def execute(self):
        self.repository.delete_by_id(self.id)