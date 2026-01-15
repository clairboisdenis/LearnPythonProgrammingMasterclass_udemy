# Enumerate Functions
#enumerates returns each item, with its index position

available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi",
                   "dvd drive"]

valid_choices = [str(i) for i in range(1, len(available_parts) +1)]
print(valid_choices)


current_choice = "-"

computer_parts = []

while current_choice != "0":
    if current_choice in valid_choices:
        print("Adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)

    else:
        print("Please add options from the list below : ")
        #for part in available_parts:
        #    print("- {0} : {1} ".format(available_parts.index(part) + 1, part ))
        for number, part in enumerate(available_parts):
            print("- {0} : {1} ".format(number + 1, part))

    current_choice = input("choose the parts you want, please : ")
else:
    print(computer_parts)

