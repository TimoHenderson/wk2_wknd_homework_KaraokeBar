import unittest
from src.transaction import Transaction
from src.guest import Guest


class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Tim", 20.00)
        self.transaction = Transaction("entry", self.guest, 5.00)

    def test_has_item(self):
        actual = self.transaction.item
        expected = "entry"
        self.assertEqual(actual, expected)
