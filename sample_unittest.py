import unittest


class MoveTests(unittest.TestCase):
    def test_five_plus_five(self):
        assert 5 + 5 == 10

    def test_one_plus_one(self):
        assert not 1 + 1 == 3

# This makes the test run all by itself when we run the script.
# Otherwise we would use python -m unittest tests.py to call script/test
if __name__ == '__main__':
    unittest.main()