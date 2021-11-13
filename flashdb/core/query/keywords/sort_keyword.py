from typing import Set, Dict

from flashdb.core.helpers.dict_helper import with_lower_keys
from flashdb.core.query.exceptions.query_exception import EmptyValueError, ValidationError
from flashdb.core.query.keywords.base import Keyword
from flashdb.core.query.operator import Order


class SortKeyword(Keyword):

    DEFAULT_VALUE = Order.ASC

    def __init__(self, s_query: Dict):
        self.data = with_lower_keys(s_query) if s_query else {}
        self.keys = self.data.keys()
        self.name = None
        self.order = self.DEFAULT_VALUE

    @staticmethod
    def mappings() -> Set:
        return {
            "name",
            "order"
        }

    def validate(self) -> "SortKeyword":
        if not self.keys:
            return self
        if 'name' not in self.keys:
            raise ValidationError("[SORT] `name` is mandatory")
        if not self.data['name']:
            raise EmptyValueError(f"[SORT] Empty `name` is not allowed")
        order = self.data.get('order', None)
        if order and not Order.from_str(order):
            raise ValidationError(f"[SORT] Incorrect or missing value for `order`. Available values are: {Order.ASC.value, Order.DESC.value}")
        return self

    def parse(self):
        self.name = self.data['name']
        if 'order' in self.data:
            self.order = Order.from_str(self.data['order'])
        return self
