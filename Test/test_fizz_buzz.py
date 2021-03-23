import unittest
from unittest import TestCase
from Main import fizzbuzz

class TestGame(TestCase):
    def test_game_int(self):
        finput, binput, ninput = 1, 2, 3
        result = fizzbuzz.the_game(finput, binput, ninput )
        self.assertEqual(result, "fizz\nfizz buzz\nfizz\n")

    def test_setup(self):
        fizz_result = type(fizzbuzz.the_setup("fizz"))
        self.assertEqual(fizz_result, int)


if __name__ == "__main__":
    unittest.main()

