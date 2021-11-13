from flashdb.core.helpers.dict_helper import with_lower_keys
from flashdb.core.query.keywords import KEYWORDS


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
        for key in KEYWORDS:
            keyword = KEYWORDS[key](self.query.get(key, None)).validate()
            setattr(self, key, keyword)

    def parse(self):
        pass

