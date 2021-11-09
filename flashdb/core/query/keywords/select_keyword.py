from typing import Set, List

from flashdb.core.query.exceptions.parse_exception import ParseException
from flashdb.core.query.keywords.base import Keyword


class SelectKeyword(Keyword):

    @staticmethod
    def mappings() -> Set:
        return {
            "name",
            "as",
            "apply_function"
        }

    def __init__(self, s_query: List):
        self.data = s_query

    def validate(self, keys):
        diff_keys = keys - self.mappings()
        if not diff_keys:
            raise ParseException(f"Incorrect or missing keys. Available values are: {','.join(self.mappings())}")

    def parse(self):
        for s_column in self.data:
            self.validate()
        return self
