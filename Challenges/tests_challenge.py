# Import the unittest module
import unittest


# Create a TestCase named SimpleTestCase with a simple test
# that asserts that 10 - 10 == 0.
# Remember unittest test names have to start with test_
class SimpleTestCase(unittest.TestCase):
    def test_challenge(self):
        assert 10 - 10 == 0