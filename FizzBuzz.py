#FizzBuzz
def game_input(fizz_input_num, buzz_input_num, num_range):
    fizz_input = int(input("What number do you want to use for Fizz? "))
    buzz_input = int(input("What number do you want to use for Buzz? "))
    num_range = int(input("How high do you want to count? "))


def fizz_buzz_game(num_range, fizz_input, buzz_input):
    for n in range(1, num_range + 1):
        if n % fizz_input == 0 and n % buzz_input == 0:
            print("fizz buzz")
        elif n % fizz_input == 0:
            print("fizz")
        elif n % buzz_input == 0:
            print("buzz")
        else:
            print(n)

fizz_buzz_game()
