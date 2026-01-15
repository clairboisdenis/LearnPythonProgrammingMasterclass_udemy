current_choice =  "-"

computer_parts = []

while current_choice != "0":
    if current_choice in "123456":
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


    else:
        print("Please add options from the list below : ")
        print("1:\tcomputer")
        print('2:\tmonitor')
        print("3:\tkeyboard")
        print("4:\tmouse")
        print("5:\tmouse mat")
        print("6:\thdmi")
        print("0:\tto finish")


    current_choice = input("choose the parts you want, please : ")
else:
    print(computer_parts)