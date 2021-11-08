from typing import Set

from flashdb.core.query.keywords.base import Keyword


class AggregateByKeyword(Keyword):

    @staticmethod
    def mappings() -> Set:
        pass

    def __init__(self, s_query: str = None):
        self.data = s_query
        self.group_name = None

    def parse(self):
        self.group_name = self.data
        return self
