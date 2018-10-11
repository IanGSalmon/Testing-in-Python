import unittest

import moves


class MoveTests(unittest.TestCase):
    def setUp(self):
        self.rock = moves.Rock()
        self.paper = moves.Paper()
        self.scissors = moves.Scissors()
    def test_five_plus_five(self):
        assert 5 + 5 == 10

    def test_one_plus_one(self):
        assert not 1 + 1 == 3

    def test_equal(self):
        # Redundant but correct
        #rock1 = moves.Rock()
        #rock2 = moves.Rock()
        #self.assertEqual(rock1, rock2)
        self.assertEqual(self.rock, moves.Rock())

    def test_not_equal(self):
        #rock = moves.Rock()
        #paper = moves.Paper()
        #self.assertNotEqual(rock, paper)
        self.assertNotEqual(self.rock, self.paper)

    def test_rock_better_than_scissors(self):
        self.assertGreater(self.rock, self.scissors)

    def test_paper_worse_than_scissors(self):
        self.assertLess(self.paper, self.scissors)

# This makes the test run all by itself when we run the script.
# Otherwise we would use python -m unittest tests.py to call script/test
if __name__ == '__main__':
    unittest.main()