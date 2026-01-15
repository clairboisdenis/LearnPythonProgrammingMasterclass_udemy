def banner_text(text):
    screen_width = 80
    if len(text) > screen_width - 4:
        print("EEK!!")
        print("The text is too long to fit in the specified width.")

    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        #output_string = "**{0}**".format(text.center(screen_width - 4))
        output_string = "**{0}**".format(centred_text)
        print(output_string)


banner_text("Hello everybody!!!! ")
banner_text("*")

numbers = [4, 23, 56, 85,21, 35, 17, 58]
print(numbers.sort())  # sort() doesn't return a value but only sort a list

numbers.sort()
print(numbers)

