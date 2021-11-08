from typing import Set

from flashdb.core.query.exceptions.parse_exception import ParseException
from flashdb.core.query.keywords.base import Keyword


class LimitKeyword(Keyword):

    @staticmethod
    def mappings() -> Set:
        pass

    def __init__(self, s_query: str = None):
        self.data = s_query
        self.limit = None

    def parse(self):
        if not self.data:
            return self
        try:
            self.limit = int(self.data)
        except ValueError:
            raise ParseException(f"{self.data} is not a number")
        return self
