

#available_exits = ["north", "south", "east", "west"]

#chosen_exit = ""

#while chosen_exit not in available_exits:
#    chosen_exit = input("Please choose a direction : ")
#    if chosen_exit.casefold() == "quit":
#        print("Game Over")
#        break
#else:
#    print("arent'you glad got out of here?")

print("Please choose your option from the list below: ")
print("1:\tLearn python")
print("2:\tLearn Java")
print("3:\tGo swimming")
print("4:\tHave dinner")
print("5:\tGo to bed")
print("0:\tExit")

choice = " "

while choice not in "12345":
    choice = input()

    if choice == "0":
        break
    elif choice in "12345" :
         print(f"You choose {choice} ")
else:
    print("You made a correct choice , thank you!!!")
