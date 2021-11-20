from enum import Enum
from typing import Set, Dict

from flashdb.core.helpers.dict_helper import with_lower_keys
from flashdb.core.query.exceptions.query_exception import ValidationError
from flashdb.core.query.keywords.base import Keyword
from flashdb.core.query.operator import Operator


class WhereKeyword(Keyword):

    def __init__(self, s_query: Dict = None):
        self.data = with_lower_keys(s_query) if s_query else {}
        self.keys = self.data.keys()
        self.default_operator = Operator.AND
        self.filters = list()

    def validate(self) -> "WhereKeyword":
        if not self.data:
            return self
        if 'filters' not in self.keys:
            raise ValidationError(f"[WHERE] `filters` is mandatory")
        operator = self.data.get('operator', None)
        if operator and not Operator.from_str(operator):
            raise ValidationError(f"[WHERE] Incorrect or missing value for `operator`. Available values are: {Operator.AND}, {Operator.OR}")
        for f in self.data['filters']:
            _ope = f.get('operator', None)
            if _ope and not Operator.from_str(_ope):
                raise ValidationError(f"[WHERE] Incorrect or missing value for `operator`. Available values are: {Operator.AND}, {Operator.OR}")
            conditions = f.get('conditions', None)
            if not conditions:
                raise ValidationError(f"[WHERE] Missing value for `conditions`.")
            if not isinstance(conditions, list):
                raise ValidationError(f"[WHERE] {conditions} is not a list")
        return self

    def parse(self):
        return self
