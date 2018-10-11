import unittest

from string_fun import is_palindrome

# Complete first test using assertTrue
# Complete second test using assertFalse

class PalindromeTestCase(unittest.TestCase):
    def test_good_palindrome(self):
        self.assertTrue(is_palindrome('tacocat'))
      
    def test_bad_palindrome(self):
        self.assertFalse(is_palindrome('cat'))

# The get_anagrams() function takes one or more words and returns anagrams for each of them as a list.
# Finish test_in_anagrams() test to check that anagrams for string "treehouse" contain word "house".

# Conversely, we shouldn't see word "code" in anagrams for "treehouse". 
# Add a new test named test_not_in_anagrams
# Use self.assertNotIn() to make sure "code" isn't in anagrams for "treehouse".

# Our get_anagrams() function raises a ValueError when you pass it an empty string.
# Finish the test to make sure this happens. You'll want to use assertRaises.

# Now add a new test, test_no_args that should also assertRaises(ValueError).
# This time call get_anagrams() with no arguments.

class AnagramTests(unittest.TestCase):
    def test_in_anagrams(self):
        self.assertIn('house', get_anagrams('treehouse'))

    def test_not_in_anagrams(self):
        self.assertNotIn('code', get_anagrams('treehouse'))

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            get_anagrams('')

     def test_no_args(self):
        with self.assertRaises(ValueError):
            get_anagrams()

if __name__ == '__main__':
    unittest.main()