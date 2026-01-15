# Hello
day = "Monday"
temperature = 30
raining = True

if day == "Saturday" and temperature >27 and not raining:
    print("Go swimming")
else:
    print("Learn Python")

if day == "Monday" and temperature > 27 or not raining:
    print("Go swimming")
else:
    print("Learn Python")

if day == "Monday" and temperature > 31 or not raining:
    print("Go swimming")
else:
    print("Learn Python")

if (day == "Monday" and not temperature > 31) or not raining:
    print("Go swimming")
else:
    print("Learn Python")



