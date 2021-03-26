from abc import ABC, abstractmethod

class TokenRepository(ABC):

    @abstractmethod
    def add(self, token):
        pass
