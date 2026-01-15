def banner_text(text=" ", screen_width=100):

    if len(text) > screen_width - 4:
        #print("EEK!!")
        #print("The text is too long to fit in the specified width.")
        raise ValueError("String {0} is larger then "
                         "specified width {1} ".format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        #output_string = "**{0}**".format(text.center(screen_width - 4))
        output_string = "**{0}**".format(centred_text)
        print(output_string)


banner_text("*")
banner_text("Hello everybody, I am happy to meet yo on this day!!!! Thank you !!!! ")
banner_text()