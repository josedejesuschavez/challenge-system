from abc import ABC, abstractmethod

class UserRepository(ABC):

    @abstractmethod
    def add(self, user):
        pass

    @abstractmethod
    def update(self, user):
        pass

    @abstractmethod
    def delete(self, user):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def is_user_valid(self, user):
        pass