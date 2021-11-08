from flashdb.core.query.exceptions.parse_exception import ParseException
from flashdb.core.query.keywords.base import Keyword


class SelectKeyword(Keyword):

    __format = {
        "name",
        "as",
        "apply_function"
    }

    def __init__(self, s_query: dict):
        self.select = s_query
        self.keys = s_query.keys()

    def validate(self):
        diff_keys = self.keys - self.__format
        if not diff_keys:
            raise ParseException(f"Incorrect or missing keys. Available values are: {','.join(self.__format)}")

    def parse(self):
        self.validate()
        return self
