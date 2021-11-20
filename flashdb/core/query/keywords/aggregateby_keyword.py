from typing import Set

from flashdb.core.query.exceptions.query_exception import EmptyValueError
from flashdb.core.query.keywords.base import Keyword


class AggregateByKeyword(Keyword):

    def __init__(self, s_query: str = None):
        self.group_name = s_query

    def validate(self) -> "AggregateByKeyword":
        if self.group_name is not None and not len(self.group_name):
            raise EmptyValueError("[AGGREGATE_BY] Empty `aggregate_by` is not allowed")
        return self

    def parse(self):
        return self
