import unittest

from flashdb.core.query.exceptions.query_exception import ParseException
from flashdb.core.query.keywords.index_keyword import IndexKeyword


class TestIndexKeyword(unittest.TestCase):

    def test_parse_success(self):
        index = IndexKeyword("myIndex")
        index.validate()

    def test_parse_valueNotInteger_throwException(self):
        index = IndexKeyword()
        with self.assertRaises(ParseException):
            index.validate()


if __name__ == "__main__":
    unittest.main()
