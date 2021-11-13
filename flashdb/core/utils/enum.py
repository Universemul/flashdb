from enum import Enum


class EnumOnSteroid(Enum):

    @classmethod
    def from_str(cls, label: str):
        try:
            return cls[label.upper()]
        except KeyError:
            return None
