import unittest

from flashdb.core.query.exceptions.query_exception import EmptyValueError, ValidationError
from flashdb.core.query.query_parser import QueryParser


class TestQueryParser(unittest.TestCase):

    def test_validate_success(self):
        qp = QueryParser({
            'select': [
                {
                    'name': 'age'
                }
            ],
            'sort': {
                'name': 'age',
                'order': 'desc'
            },
            'index': 'Person',
            'limit': 4,
            'aggregate_by': 'myColumn2'
        })
        qp.validate()

    def test_validate_withoutNotMandatoryKeywords_success(self):
        qp = QueryParser({
            'select': [
                {
                    'name': 'age'
                }
            ],
            'index': 'Person',
        })
        qp.validate()

    def test_validate_withoutSortName_throwException(self):
        qp = QueryParser({
            'select': [
                {
                    'name': 'age'
                }
            ],
            'index': 'Person',
            'sort': {
                'order': "asc"
            }
        })
        with self.assertRaises(ValidationError):
            qp.validate()

    def test_validate_withEmptyLimit_throwException(self):
        qp = QueryParser({
            'select': [
                {
                    'name': 'age'
                }
            ],
            'index': 'Person',
            'limit': ''
        })
        with self.assertRaises(EmptyValueError):
            qp.validate()


if __name__ == "__main__":
    unittest.main()
