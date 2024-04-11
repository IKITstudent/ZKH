import abc
from abc import ABC, abstractmethod

class AbstractRepository(ABC):
    @abstractmethod
    def save_item(self, item):
        pass
    @abstractmethod
    def get_item(self, item):
        pass
