i = 0

while i < 10:
    print("is is now {0}".format(i))
    i += 1



# 67 Advanced while loops

available_exits = ["north", "south", "east", "west"]

chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please  choose a diretion, please ! ")
    if chosen_exit.casefold() == "quit":
        print("Game Over !!!!!!!!!!!!")
        break


print("aren't you glad you got out of there by taking the {} diretcion ".format(chosen_exit))


