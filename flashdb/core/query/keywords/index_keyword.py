from typing import Set

from flashdb.core.query.exceptions.parse_exception import ParseException
from flashdb.core.query.keywords.base import Keyword


class IndexKeyword(Keyword):

    @staticmethod
    def mappings() -> Set:
        pass

    def __init__(self, s_query: str = None):
        self.data = s_query
        self.index = None

    def validate(self):
        if not self.data:
            raise ParseException("An index is needed to perfom the query")

    def parse(self):
        self.validate()
        self.index = self.data
