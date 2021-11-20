from typing import List

from flashdb.core.query.exceptions.query_exception import ParseException, EmptyValueError, ValidationError
from flashdb.core.query.functions import VALID_FUNCTIONS
from flashdb.core.query.keywords.base import Keyword


class Column(object):

    def __init__(self, name: str, alias: str = None, functions: List = None):
        self.name = name
        self.alias = alias
        self.functions = functions

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            print(other.__dict__)
            return other.__dict__ == self.__dict__
        return False


class SelectKeyword(Keyword):

    NAME = "name"
    AS = "as"
    FUNCTION = "apply_function"
    FUNCTION_DELIMITER = '>'

    def __init__(self, s_query: List):
        self.data = s_query
        self.columns = []

    def validate(self) -> "Keyword":
        for item in self.data:
            keys = item.keys()
            if self.NAME not in keys:
                raise ValidationError(f"[SELECT] `{self.NAME}` is mandatory")
            if not item[self.NAME]:
                raise EmptyValueError(f"[SELECT] Empty `{self.NAME}` is not allowed")
            for keyword in [self.AS, self.FUNCTION]:
                if keyword in keys and not item[keyword]:
                    raise EmptyValueError(f"[SELECT] Empty `{keyword}` is not allowed")
        return self

    def parse(self):
        if not self.data:
            return
        for item in self.data:
            self.columns.append(Column(
                item[self.NAME],
                item.get(self.AS, None),
                self.parse_functions(item.get(self.FUNCTION, None))
            ))
        return self

    def parse_functions(self, raw_functions: str):
        if raw_functions is None:
            return None
        split_functions = raw_functions.split(self.FUNCTION_DELIMITER)
        if any(f not in VALID_FUNCTIONS for f in split_functions):
            raise ParseException(f"[SELECT] {raw_functions} is invalid")
        functions = list()
        for f_name in split_functions:
            functions.append(VALID_FUNCTIONS[f_name]())
        return functions
