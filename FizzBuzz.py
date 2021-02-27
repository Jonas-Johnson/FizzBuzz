#FizzBuzz
def fizz_buzz_game():
    fizz_input_num = input("What number do you want to use for Fizz?")
    buzz_input_num = input("What number do you want to use for Buzz?")
    num_range = input("How high do you want to count?")

    for n in range(1,int(num_range) + 1):
        if n % int(fizz_input_num) == 0 and n % int(buzz_input_num) == 0:
            print("fizz buzz")
        elif n % int(fizz_input_num) == 0:
            print("fizz")
        elif n % int(buzz_input_num) == 0:
            print("buzz")
        else:
            print(n)

fizz_buzz_game()
