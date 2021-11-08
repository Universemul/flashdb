import unittest

from flashdb.core.query.exceptions.parse_exception import ParseException
from flashdb.core.query.keywords.sort_keyword import SortKeyword


def get_valid_sort(order: str = SortKeyword.Order.ASC.value) -> SortKeyword:
    return SortKeyword({
        "name": "test",
        "order": order
    })


def get_invalid_sort_with_no_name_key():
    return SortKeyword({
        'order': SortKeyword.Order.ASC.value
    })


class TestSortKeyword(unittest.TestCase):

    def test_parse_success(self):
        sort = get_valid_sort()
        sort.parse()
        self.assertEqual("test", sort.name)
        self.assertEqual(SortKeyword.Order.ASC, sort.order)

    def test_parse_descOrder_success(self):
        sort = get_valid_sort(SortKeyword.Order.DESC.value)
        sort.parse()
        self.assertEqual(SortKeyword.Order.DESC, sort.order)

    def test_parse_sortWithNoNameKey_throwException(self):
        sort = get_invalid_sort_with_no_name_key()
        with self.assertRaises(ParseException):
            sort.parse()

    def test_parse_invalidOrder_throwException(self):
        sort = SortKeyword({'name': 'test', 'order': 'toto'})
        with self.assertRaises(ParseException):
            sort.parse()
