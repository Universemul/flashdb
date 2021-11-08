from abc import ABC, abstractmethod
from typing import Set


class Keyword(ABC):

    @staticmethod
    @abstractmethod
    def mappings() -> Set:
        pass
