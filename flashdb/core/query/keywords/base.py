from abc import ABC, abstractmethod
from typing import Set


class Keyword(ABC):

    @staticmethod
    @abstractmethod
    def mappings() -> Set:
        pass

    @abstractmethod
    def validate(self) -> "Keyword":
        pass
