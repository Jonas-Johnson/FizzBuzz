from Main import fizzbuzz

if __name__ == "__main__":
    fizz_result = fizzbuzz.fizz_setup()
    buzz_result = fizzbuzz.buzz_setup()
    range_result = fizzbuzz.range_setup()
    result = fizzbuzz.the_game(fizz_result, buzz_result, range_result)
    print(result)
