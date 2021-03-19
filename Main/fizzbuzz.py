#fizz buzz the game

def get_input(text):
    return input(text)

def the_setup():
    try:
        fizz_input = int(get_input("What number do you want to use for Fizz? "))
        buzz_input = int(get_input("What number do you want to use for Buzz? "))
        num_range = int(get_input("How high do you want to count? "))
        return fizz_input, buzz_input, num_range

    except ValueError:
        print("No good, please try again.")
        the_setup()



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

