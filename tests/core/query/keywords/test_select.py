import unittest

from flashdb.core.query.exceptions.query_exception import EmptyValueError
from flashdb.core.query.keywords.select_keyword import SelectKeyword


class TestSelectKeyword(unittest.TestCase):

    def test_validate_success(self):
        expected = {
            "name": "myColumn",
            "as": "toto",
            "apply_function": "avg>length"
        }
        SelectKeyword([expected]).validate()

    def test_validate_emptyName_throwException(self):
        with self.assertRaises(EmptyValueError):
            SelectKeyword([{
                "name": ""
            }]).validate()

    def test_validate_emptyAs_throwException(self):
        with self.assertRaises(EmptyValueError):
            SelectKeyword([{
                "name": "myColumn",
                "as": ""
            }]).validate()


if __name__ == "__main__":
    unittest.main()
