from abc import ABC, abstractmethod
from typing import Set


class Keyword(ABC):

    @abstractmethod
    def mappings(self) -> Set:
        pass
