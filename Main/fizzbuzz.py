# fizz buzz the game
def the_setup(name):
    user_input = None
    while user_input is None:
        try:
            user_input = int(input(f"What number do you want to use for {name}? "))
        except ValueError:
            print("That was not a number, please try again.")
    return user_input


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
