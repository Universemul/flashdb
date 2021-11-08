import unittest

from flashdb.core.query.query_parser import QueryParser
from flashdb.core.query.keywords.sort_keyword import SortKeyword


class TestQueryParser(unittest.TestCase):

    def test_parse_success(self):
        qp = QueryParser({
            'sort': {
                'name': 'myColumn',
                'order': 'desc'
            },
            'limit': 4,
            'aggregate_by': 'myColumn2'
        })
        qp.parse()
        self.assertEqual("myColumn", qp.sort.name)
        self.assertEqual(SortKeyword.Order.DESC, qp.sort.order)
        self.assertEqual(4, qp.limit.limit)
        self.assertEqual("myColumn2", qp.aggregate_by.group_name)


if __name__ == "__main__":
    unittest.main()
