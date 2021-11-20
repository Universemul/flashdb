import unittest
from typing import Dict

from parameterized import parameterized

from flashdb.core.query.exceptions.query_exception import EmptyValueError, ParseException
from flashdb.core.query.functions import Length, Avg
from flashdb.core.query.keywords.select_keyword import SelectKeyword, Column


class TestSelectKeyword(unittest.TestCase):

    def test_validate_success(self):
        expected = {
            "name": "myColumn",
            "as": "toto",
            "apply_function": "avg>length"
        }
        SelectKeyword([expected]).validate()

    @parameterized.expand([
        ({"name": ""}, EmptyValueError),
        ({"name": "myColumn", "as": ""}, EmptyValueError),
        ({"name": "myColumn", "apply_function": ""}, EmptyValueError),
    ])
    def test_validate_emptyFieldInItem_throwException(self, item: Dict, expected_exception: Exception):
        with self.assertRaises(expected_exception):
            SelectKeyword([item]).validate()

    def test_parse_success(self):
        expected = Column("myColumn", "toto", [
            Avg(), Length()
        ])
        select = SelectKeyword([{
            "name": "myColumn",
            "as": "toto",
            "apply_function": "avg>length"
        }]).parse()
        self.assertEqual(1, len(select.columns))
        self.assertEqual(expected, select.columns[0])

    def test_parse_unknownFunction_throwException(self):
        with self.assertRaises(ParseException):
            SelectKeyword([{
                "name": "myColumn",
                "as": "toto",
                "apply_function": "dfdf"
            }]).parse()


if __name__ == "__main__":
    unittest.main()
