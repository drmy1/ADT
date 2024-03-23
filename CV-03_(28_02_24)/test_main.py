import unittest
from main import test_operation_in


class TestMain(unittest.TestCase):

    def test_in_empty(self):
        collection = []
        self.assertFalse(test_operation_in(collection))

    def test_in_not_present(self):
        collection = [1, 2, 3]
        self.assertFalse(test_operation_in(collection))

    def test_in_present(self):
        collection = [1, 2, 3]
        collection.append(2)
        self.assertTrue(test_operation_in(collection))
