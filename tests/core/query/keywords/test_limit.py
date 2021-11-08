import unittest

from flashdb.core.query.exceptions.parse_exception import ParseException
from flashdb.core.query.keywords.limit_keyword import LimitKeyword


class TestLimitKeyword(unittest.TestCase):

    def test_parse_success(self):
        limit = LimitKeyword("3")
        limit.parse()
        self.assertEqual(3, limit.limit)

    def test_parse_valueNotInteger_throwException(self):
        limit = LimitKeyword("st")
        with self.assertRaises(ParseException):
            limit.parse()


if __name__ == "__main__":
    unittest.main()
