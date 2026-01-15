import random

highest = 20

answer = random.randint(1, 20)
print("The answer is {0} ".format(answer))

guess = None

while guess != answer:
    guess = int(input("Please give a number between  0 and 20 "))
    if guess < 0 or guess > 20:
        guess = int(input("The given value is incorrect, please give a number between  0 and 20 "))
    if guess ==  answer:
        print("You got it first time")
        break
    elif guess < answer:
        print("Please guess higher ")
        guess = int(input("Please give a number between  0 and 20 "))
    elif guess > answer:
        guess = int(input("Please give a number lower than {0} ".format(guess)))
