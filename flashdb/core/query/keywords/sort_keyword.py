import enum
from typing import Set

from flashdb.core.helpers.dict_helper import with_lower_keys
from flashdb.core.query.exceptions.parse_exception import ParseException
from flashdb.core.query.keywords.base import Keyword


class SortKeyword(Keyword):

    class Order(enum.Enum):
        ASC = "asc"
        DESC = "desc"

        @staticmethod
        def from_str(label):
            if label == "asc":
                return SortKeyword.Order.ASC
            if label == "desc":
                return SortKeyword.Order.DESC
            return None

    DEFAULT_VALUE = Order.ASC

    def __init__(self, s_query: dict):
        self.data = with_lower_keys(s_query)
        self.keys = s_query.keys()
        self.name = None
        self.order = SortKeyword.Order.ASC

    @staticmethod
    def mappings() -> Set:
        return {
            "name",
            "order"
        }

    def validate(self):
        diff_keys = self.keys ^ SortKeyword.mappings()
        if diff_keys:
            raise ParseException(f"Incorrect or missing keys. Available values are: {','.join(self.mappings())}")
        order = self.data.get('order', None)
        if order and not SortKeyword.Order.from_str(order):
            raise ParseException(f"Incorrect or missing value for order. Available values are: {SortKeyword.Order.ASC, SortKeyword.Order.DESC}")

    def parse(self):
        self.validate()
        self.name = self.data['name']
        if 'order' in self.data:
            self.order = SortKeyword.Order.from_str(self.data['order'])
        return self
