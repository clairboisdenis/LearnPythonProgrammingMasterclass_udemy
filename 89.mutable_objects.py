# list
# dict
# set
# Bytearray

shopping_list = ["milk",
                 "pasta,"
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]

another_list = shopping_list

print(shopping_list)
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))  # stay with same id => The id remains unchanged

print(another_list)

a = b = c = d = e = f = g = another_list
print(a, b, c, d, e, f, g)

listb = [a, b, c, d, e, f, g]

print(listb)

print(listb[2][-1])

listb[2].append("coffie")

print(listb[2][-1])
print(listb)
print("---------------")

print(listb)
print(listb[2])

new_coffie = listb[2]
print(new_coffie)

new_coffie.append(new_coffie)

print(new_coffie)

