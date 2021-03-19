import unittest
from unittest import TestCase
from Main import fizzbuzz

class TestGame(TestCase):
    def test_game_int(self):
        finput, binput, ninput = 1, 2, 3
        result = fizzbuzz.the_game(finput, binput, ninput )
        self.assertEqual(result, "fizz\nfizz buzz\nfizz\n")


if __name__ == "__main__":
    unittest.main()

