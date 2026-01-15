import random

highest = 10
answer = random.randint(1, highest)

print("The random value is {0} ".format(answer))

print("Please guess a number between 1  and {0} ".format(highest))
guess = int(input())

print("The value of the guess number is {0} ".format(guess))

if guess == answer:
    print("You got it at first time !!!")
elif guess < answer:
    print("Please guess higher!!!")
    guess = int(input())
    if guess == answer:
        print("You got it at first time !!!")
elif guess > answer:
    print("Please guess lower!!!")
    guess = int(input())
    if guess == answer:
        print("You got it at first time !!!")
