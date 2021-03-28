import unittest
from unittest import mock
from unittest import TestCase
from Main import fizzbuzz


class TestGame(TestCase):
    def test_game_int(self):
        finput, binput, ninput = 1, 2, 3
        result = fizzbuzz.the_game(finput, binput, ninput)
        self.assertEqual(result, "fizz\nfizz buzz\nfizz\n")

    def test_the_setup(self):
        with mock.patch("builtins.input", return_value="3"):
            assert fizzbuzz.the_setup("fizz") == int(3)
        with mock.patch("builtins.input", side_effect=[3, 6, 34]):
            assert fizzbuzz.the_setup("fizz") == int(3)
            assert fizzbuzz.the_setup("buzz") == int(6)
            assert fizzbuzz.the_setup("the upper limit") == int(34)


if __name__ == "__main__":
    unittest.main()
