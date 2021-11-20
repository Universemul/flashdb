from abc import ABC


class Function(ABC):

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return getattr(other, "name") == getattr(self, "name")
        return False
