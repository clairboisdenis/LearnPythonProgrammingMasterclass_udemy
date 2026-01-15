parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("{0} is in the word : {1} !!!!!!".format(letter, parrot))
elif letter not in parrot:
    print("The letter {0} is not in the word {1} !!! ".format(letter,parrot))
else:
    print("I don't need that letter")