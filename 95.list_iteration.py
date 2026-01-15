

available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi",
                   "dvd drive"]



current_choice =  "-"

computer_parts = []

while current_choice != "0":
    if current_choice in "1234567":
        print("Adding {}".format(current_choice))
        if current_choice == '1':
            computer_parts.append("computer")
        elif current_choice == '2':
            computer_parts.append("monitor")
        elif current_choice == '3':
            computer_parts.append("keyboard")
        elif current_choice == '4':
            computer_parts.append("mouse")
        elif current_choice == '5':
            computer_parts.append("mouse mat")
        elif current_choice == '6':
            computer_parts.append("hdmi")
        elif current_choice == '7':
            computer_parts.append("dvd drive")

    else:
        print("Please add options from the list below : ")
        for part in available_parts:
            print("- {0} : {1} ".format(available_parts.index(part) + 1, part ))



    current_choice = input("choose the parts you want, please : ")
else:
    print(computer_parts)