from abc import ABC, abstractmethod


class Keyword(ABC):

    @abstractmethod
    def validate(self) -> "Keyword":
        pass
