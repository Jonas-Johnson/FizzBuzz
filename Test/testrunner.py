import pytest
from Main import fizzbuzz


def test_game_int(self):
    finput, binput, ninput = 1, 2, 3
    result = fizzbuzz.the_game(finput, binput, ninput )
    self.assertEqual(result, "fizz\nfizz buzz\nfizz\n")

def test_setup(self):
    #test if input is an integer... How to check if input is an integer? call type()?
    fizz_result = type(fizzbuzz.fizz_setup())
    self.assertEqual(fizz_result, int)
    buzz_result = type(fizzbuzz.fizz_setup())
    self.assertEqual(buzz_result, int)
    num_result = type(fizzbuzz.fizz_setup())
    self.assertEqual(num_result, int)