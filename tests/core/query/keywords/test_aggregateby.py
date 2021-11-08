import unittest

from flashdb.core.query.keywords.aggregateby_keyword import AggregateByKeyword


class TestAggregateByKeyword(unittest.TestCase):

    def test_parse_success(self):
        expected = 'myColumn'
        aggregation = AggregateByKeyword(expected).parse()
        self.assertEqual(expected, aggregation.group_name)


if __name__ == "__main__":
    unittest.main()
