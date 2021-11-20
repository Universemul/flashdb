from typing import Set, List, Dict

from flashdb.core.query.exceptions.query_exception import ParseException, EmptyValueError, ValidationError
from flashdb.core.query.keywords.base import Keyword


class SelectKeyword(Keyword):

    def __init__(self, s_query: List):
        self.data = s_query
        self.columns = []

    def validate(self) -> "Keyword":
        for item in self.data:
            keys = item.keys()
            if 'name' not in keys:
                raise ValidationError("[SELECT] `name` is mandatory")
            if not item['name']:
                raise EmptyValueError(f"[SELECT] Empty `name` is not allowed")
            if 'as' in keys and not item['as']:
                raise EmptyValueError(f"[SELECT] Empty `as` is not allowed")
            # check if function exists
        return self

    def parse(self):
        if not self.data:
            return
        for item in self.data:
            self.columns.append({
                'name': item['name'],
                'as': item.get('as', None),
                'functions': None  # create function with a split
            })
        return self
