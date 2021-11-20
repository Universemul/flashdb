import unittest

from flashdb.core.query.exceptions.query_exception import EmptyValueError
from flashdb.core.query.keywords.aggregateby_keyword import AggregateByKeyword


class TestAggregateByKeyword(unittest.TestCase):

    def test_validate_success(self):
        expected = 'myColumn'
        AggregateByKeyword(expected).validate()

    def test_validate_emptyValue_throwException(self):
        with self.assertRaises(EmptyValueError):
            AggregateByKeyword("").validate()


if __name__ == "__main__":
    unittest.main()
