from typing import Set

from flashdb.core.query.exceptions.query_exception import ParseException
from flashdb.core.query.keywords.base import Keyword


class IndexKeyword(Keyword):

    @staticmethod
    def mappings() -> Set:
        pass

    def __init__(self, s_query: str = None):
        self.index = s_query

    def validate(self) -> "Keyword":
        if not self.index:
            raise ParseException("[INDEX] An index is needed to perform the query")
        return self

    def parse(self):
        return self
