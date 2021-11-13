import unittest

from flashdb.core.query.exceptions.query_exception import ValidationError
from flashdb.core.query.keywords import WhereKeyword
from flashdb.core.query.operator import Operator


# region Misc

def get_valid_where(operator: str = Operator.AND.value) -> WhereKeyword:
    return WhereKeyword({
        'operator': operator,
        "filters": [
            {
                'operator': Operator.OR.value,
                'conditions': [
                    "myColumn == 'test'"
                ]
            }
        ]
    })


def get_invalid_where_with_no_filters_key():
    return WhereKeyword({
        'operator': Operator.AND.value
    })


# endregion


class TestWhereKeyword(unittest.TestCase):

    def test_validate_success(self):
        where = get_valid_where()
        where.validate()

    def test_validate_orOperator_success(self):
        where = get_valid_where(Operator.OR.value)
        where.validate()

    def test_validate_withNoFiltersKey_throwException(self):
        where = get_invalid_where_with_no_filters_key()
        with self.assertRaises(ValidationError):
            where.validate()

    def test_validate_conditionsNotList_throwException(self):
        where = WhereKeyword({
            'operator': Operator.AND.value,
            'conditions': {
            }
        })
        where.conditions = {}
        with self.assertRaises(ValidationError):
            where.validate()
