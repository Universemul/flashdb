from flashdb.core.helpers.dict_helper import with_lower_keys
from flashdb.core.query.keywords import KEYWORDS, SORT, LIMIT, LimitKeyword, SortKeyword, AggregateByKeyword, \
    AGGREGATE_BY


class QueryParser(object):

    # Input is the query json formatted
    def __init__(self, query: dict):
        self.query = with_lower_keys(query)
        self.keys = self.query.keys()
        self.select = None
        self.index = None
        self.where = None
        self.sort = None
        self.limit = None
        self.aggregate_by = None

    def validate(self):
        pass

    def parse(self):
        if LIMIT in self.keys:
            self.limit: LimitKeyword = KEYWORDS[LIMIT](self.query[LIMIT]).parse()
        if SORT in self.keys:
            self.sort: SortKeyword = KEYWORDS[SORT](self.query[SORT]).parse()
        if AGGREGATE_BY in self.keys:
            self.aggregate_by: AggregateByKeyword = KEYWORDS[AGGREGATE_BY](self.query[AGGREGATE_BY]).parse()
