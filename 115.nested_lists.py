menu = [
    ["eggs", "bacon"],
    ["eggs", "sausage", "bacon"],
    ["eggs", "spam"],
    ["eggs", "bacon", "spam"],
    ["eggs", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "eggs", "spam", "spam", "bacon", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"]
]

for meal in menu:
    if "spam" in meal:
        print(meal)

        for item in meal:
            print(item)

    else:
        print(" {0} has a bacon score of {1}".
              format(meal, meal.count("bacon")))


print()

for meal in menu:
    if "spam" not in meal:
        print(meal)

        for item in meal:
            print(item)
    else:
        print(" {0} has a spam score of {1}"
              .format(meal, meal.count("spam")))