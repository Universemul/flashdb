import unittest

from flashdb.core.query.exceptions.query_exception import EmptyValueError, ValidationError
from flashdb.core.query.keywords.sort_keyword import SortKeyword
from flashdb.core.query.operator import Order

# region Misc


def get_valid_sort(order: str = Order.ASC.value) -> SortKeyword:
    return SortKeyword({
        "name": "test",
        "order": order
    })

def get_invalid_sort_with_no_name_key():
    return SortKeyword({
        'order': Order.ASC.value
    })

def get_invalid_sort_with_no_order_key():
    return SortKeyword({
        'name': "test"
    })
# endregion

class TestSortKeyword(unittest.TestCase):

    def test_validate_success(self):
        sort = get_valid_sort()
        sort.validate()

    def test_validate_descOrder_success(self):
        sort = get_valid_sort(Order.DESC.value)
        sort.validate()

    def test_validate_withNoNameKey_throwException(self):
        sort = get_invalid_sort_with_no_name_key()
        with self.assertRaises(ValidationError):
            sort.validate()

    def test_validate_withNoOrderKey_expectAscOrder(self):
        sort = get_invalid_sort_with_no_order_key()
        sort.validate()

    def test_validate_invalidOrder_throwException(self):
        sort = SortKeyword({'name': 'test', 'order': 'toto'})
        with self.assertRaises(ValidationError):
            sort.validate()

    def test_validate_emptyName_throwException(self):
        with self.assertRaises(EmptyValueError):
            SortKeyword({'name': ""}).validate()
