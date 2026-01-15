import random

def get_integer(prompt):
   """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int`is entered.
   :param prompt:
   :return:
   """


    while True:
        temp = input(prompt)
        if temp.isnumeric():
            print("you nummer is {0}".format(int(temp)))
            print(f"your nummer is {int(temp)}")
            return int(temp)
        else:
            print(f"{temp} is not a valid number".format(temp))



highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing.
guess = 0  # initialise to any number that doesn't equal answer
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer("Hello give number please: ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:  # guess must be greater than answer
            print("Please guess lower")
