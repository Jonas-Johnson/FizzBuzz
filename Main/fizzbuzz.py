#fizz buzz the game


def fizz_setup():
    try:
        fizz_input = int(input("What number do you want to use for Fizz? "))
        return fizz_input

    except ValueError:
        print("That is not a number, please try again.")
        fizz_setup()


def buzz_setup():
    try:
        buzz_input = int(input("What number do you want to use for Buzz? "))
        return buzz_input

    except ValueError:
        print("That is not a number, please try again.")
        buzz_setup()


def range_setup():
    try:
        num_range = int(input("How high do you want to count? "))
        return num_range

    except ValueError:
        print("That is not a number, please try again.")
        range_setup()


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

