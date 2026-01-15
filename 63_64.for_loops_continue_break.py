shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
    if item != "spam":
        print(" article is {0}".format(item))



for item in shopping_list:
    if item == "eggs":
        continue
    print("*** Buy the item = {0}".format(item))


for item in shopping_list:
    if item == "spam":
        break
    print(" article : {0}".format(item))

item_to_find = "spam"
found_at = None

print("the legnth of the list is : {0}".format(len(shopping_list)))

for index in range (len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break

if found_at is not None:
    print("the index is {0}".format(found_at))
else:
    print("{} not found".format(found_at))


item_to_find_bis = "albatros"
found_at_bis = None


for indexb in range(len(shopping_list)):
    if shopping_list[indexb] == item_to_find_bis:
        found_at_bis = indexb
        break

if found_at_bis is not None:
    print("The index is {01} !".format(found_at_bis))
else:
    print("{} is not found in the list ".format(item_to_find_bis))



