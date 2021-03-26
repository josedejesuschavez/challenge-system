from abc import ABC, abstractmethod


class TeamMemberRepository(ABC):

    @abstractmethod
    def add(self, id, team_member):
        pass

    @abstractmethod
    def update(self, id, team_member):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def delete_by_id(self, id):
        pass