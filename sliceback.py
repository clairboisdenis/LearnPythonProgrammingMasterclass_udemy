letters =  "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]  # zyxwvutsrqponmlkjihgfedcb
print(backwards)

backwards2 = letters[25:1:-1]  # zyxwvutsrqponmlkjihgfedc
print(backwards2)

backwards3 = letters[25:-1:-1]  # nothing
print(backwards3)

backwards4 = letters[26:0:-1]  # zyxwvutsrqponmlkjihgfedcb
print(backwards4)

########## SOLUTION

backwards5 = letters[25::-1]
print(backwards5)

# OR

backwards6 = letters[::-1]
print(backwards6)

######## Challenges

# slice with "qpo"
backwards7 = letters[16:13:-1]
print(backwards7)

# slice with "edcba"
backwards8 = letters[4::-1]
print(backwards8)

# slice with the last 8 characters
backwards9 = letters[:18:-1]
print(backwards9)
#or
backwards10 =  letters[:-9:-1]

#### idioms

print(letters[:-9:-1])

print(letters[::-1])  #  zyxwvutsrqponmlkjihgfedcba

print(letters[::1])  # abcdefghijklmnopqrstuvwxyz

print(letters[-4:])   # wxyz
print(letters[-1:])  # z

print(letters[::])  # abcdefghijklmnopqrstuvwxyz

print(letters[:1])  # a    ==  print(letters[0]






