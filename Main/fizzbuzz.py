#fizz buzz the game

def fizz_setup():
    fizz_input = None
    while fizz_input is None:
        try:
            fizz_input = int(input("What number do you want to use for Fizz? "))
        except ValueError:
            print("That is not a number, please try again.")
    return fizz_input


def buzz_setup():
    buzz_input = None
    while buzz_input is None:
        try:
            buzz_input = int(input("What number do you want to use for Buzz? "))
        except ValueError:
            print("That is not a number, please try again.")
    return buzz_input


def range_setup():
    num_range = None
    while num_range is None:
        try:
            num_range = int(input("How high do you want to count? "))
        except ValueError:
            print("That is not a number, please try again.")
    return num_range


def the_game(fizz_input, buzz_input, num_range):
    results = ""
    for n in range(1, num_range + 1):
        if n % fizz_input == 0 and n % buzz_input == 0:
            results += "fizz buzz\n"
        elif n % fizz_input == 0:
            results += "fizz\n"
        elif n % buzz_input == 0:
            results += "buzz\n"
        else:
            results += str(n) + "\n"
    return results

