name = input("What's your name, please? ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age >= 18:
    print("You are old enough to vote")
else:
    print("Please " + name + " come back  in {0} years. ".format(18 - age))

if age < 18:
    print("Please " + name + " Come back in {0} years. ".format(18 - age))
elif age == 900:
    print("Sorry, Yoda, you are too old")
else:
    print("You are old enough to vote")
    print("Please, put an X in the box")