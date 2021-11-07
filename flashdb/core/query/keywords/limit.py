from flashdb.core.query.exceptions.parse_exception import ParseException
from flashdb.core.query.keywords.base import Keyword


class Limit(Keyword):

    def __init__(self, s_query: str = None):
        self.limit = s_query
        self.value = None

    def parse(self):
        if not self.limit:
            return
        try:
            self.value = int(self.limit)
        except ValueError:
            raise ParseException(f"{self.limit} is not a number")
