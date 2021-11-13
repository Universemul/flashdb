from typing import Set, Union

from flashdb.core.query.exceptions.query_exception import EmptyValueError, ParseException, ValidationError
from flashdb.core.query.keywords.base import Keyword


class LimitKeyword(Keyword):

    @staticmethod
    def mappings() -> Set:
        pass

    def __init__(self, s_query: Union[str, int] = None):
        self.data: Union[str, int] = s_query
        self.value = None

    def validate(self) -> "LimitKeyword":
        if self.data is None:
            return self
        if isinstance(self.data, int):
            if self.data <= 0:
                raise ValidationError("[LIMIT] Only positive number are allowed")
            return self
        if self.data is not None and not len(self.data):
            raise EmptyValueError("[LIMIT] Empty `limit` is not allowed.")
        if not isinstance(self.data, str):
            raise ValidationError(f"[LIMIT] {self.data} is not a number")
        if not self.data.isnumeric():
            raise ValidationError(f"[LIMIT] {self.data} is not a number")
        return self

    def parse(self):
        if not self.data:
            return self
        self.value = int(self.data) if isinstance(self.data, str) else self.data
        return self
