parrot = "Norwegian Blue"

print(parrot[0:6])
print(parrot[0:-1]) # Norwegian Blu

print(parrot[-1]) # e

print(parrot[3:4]) # w

print(parrot[3:5])

print(parrot[:9])  # Norwegian

print(parrot[3:])  # wegian

print(parrot[10:])  # Blue

print(parrot[:6] + parrot[6:])  # Norwegian Blue

print(parrot[:])  # Norwegian Blue

letters = "abcdefghijklmnopqrstuvwxyz"

print(parrot[-4:2])  # nothing is displayed

print(parrot[2:-4])  # rwegian

print(parrot[-4:-2])  # Bl

print(parrot[-2:-4])   # nothing is displayed

print(parrot[-4:12])  # Bl

print(parrot[-14:])  # Norwegian Blue

print(parrot[0:6:2])   # Nre 0->6 (not included) by 2

print(parrot[0:6:3])   # Nw 0->6 (not included) by 3

number = "9,223,372,036,854,775,807"  # ,,,,,,
print(number[1::4])

number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)

print(type(separators))






