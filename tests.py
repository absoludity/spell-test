#!/usr/bin/python
import unittest

from utils import order_words


class OrderWordsTestCase(unittest.TestCase):

    def test_order(self):
        words = ["Fee", "Fi", "Fo"]
        stats = {
            "Fee": {
                "right_count": 5,
                "total_count": 5,
                "last_attempt": None,
            },
            "Fi": {
                "right_count": 3,
                "total_count": 5,
                "last_attempt": None,
            },
            "Fo": {
                "right_count": 0,
                "total_count": 5,
                "last_attempt": None,
            },

        }

        ordered_words = order_words(words, stats)

        self.assertEqual(["Fo", "Fi", "Fee"], ordered_words)


if __name__ == '__main__':
    unittest.main()
