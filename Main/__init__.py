from Main import fizzbuzz

if __name__ == "__main__":
    fizz_result = fizzbuzz.the_setup("fizz")
    buzz_result = fizzbuzz.the_setup("buzz")
    range_result = fizzbuzz.the_setup("the upper limit")
    result = fizzbuzz.the_game(fizz_result, buzz_result, range_result)
    print(result)
