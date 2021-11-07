import enum
from typing import Set

from flashdb.core.helpers.dict_helper import with_lower_keys
from flashdb.core.query.exceptions.parse_exception import ParseException
from flashdb.core.query.keywords.base import Keyword


class Sort(Keyword):

    class Order(enum.Enum):
        ASC = "ASC"
        DESC = "DESC"

        @staticmethod
        def from_str(label):
            if label == "ASC":
                return Sort.Order.ASC
            if label == "DESC":
                return Sort.Order.DESC
            return None

    DEFAULT_VALUE = Order.ASC

    def __init__(self, s_query: dict):
        self.sort = with_lower_keys(s_query)
        self.keys = s_query.keys()

    def mappings(self) -> Set:
        return {
            "name",
            "order"
        }

    def validate(self):
        diff_keys = self.keys - self.mappings()
        if not diff_keys:
            raise ParseException(f"Incorrect or missing keys. Available values are: {','.join(self.mappings())}")
        if Sort.Order.from_str(self.sort['ORDER']) is None:
            raise ParseException(f"Incorrect or missing value for order. Available values are: {Sort.Order.ASC, Sort.Order.DESC}")

    def parse(self):
        self.validate()
