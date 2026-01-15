if 0:
    print("False")
else:
    print("True")

#### Be careful :  0 = False
####               1 = True

name = input("Please enter your name:  ")

if name:
    print("hello {0} {0} !!".format(name))
else:
    print("Are you the man with no name?")