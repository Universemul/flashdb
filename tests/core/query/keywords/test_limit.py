import unittest

from flashdb.core.query.exceptions.query_exception import EmptyValueError, ValidationError
from flashdb.core.query.keywords.limit_keyword import LimitKeyword


class TestLimitKeyword(unittest.TestCase):

    def test_validate_success(self):
        limit = LimitKeyword("3")
        limit.validate()

    def test_validate_valueNotInteger_throwException(self):
        limit = LimitKeyword("st")
        with self.assertRaises(ValidationError):
            limit.validate()

    def test_validate_emptyValue_throwException(self):
        with self.assertRaises(EmptyValueError):
            LimitKeyword("").validate()

    def test_validate_negativeValue_throwException(self):
        with self.assertRaises(ValidationError):
            LimitKeyword(-1).validate()


if __name__ == "__main__":
    unittest.main()
