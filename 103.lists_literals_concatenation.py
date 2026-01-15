empty_list = []
even = [2, 4, 6, 8]

odd = [1, 3, 5, 7, 9]

#######################
even.extend(odd)
print(even)

another_even = even
print(another_even)

even.sort(reverse=True)
print(even)
print(another_even)
print(another_even)

print(id(even))
print(id(another_even))

print(even is another_even) # True


#######################

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

digits = sorted("432985617")
print(digits)


words = sorted("Denis Clairbois")
print(words)

digits2 = list("432985617")
print(digits2)

print()
more_numbers = list(numbers)
print(numbers)

print(more_numbers)
print(numbers is more_numbers)
print(numbers == more_numbers)

print()

## slice ##

more_numbers2 = numbers[:]
print(numbers)
print(more_numbers2)
print(numbers is more_numbers2)
print(numbers == more_numbers2)

print("more_numbers_3")


## copy ##

more_numbers3 = numbers.copy()
print(numbers)
print(more_numbers3)
print(numbers is more_numbers3)
print(numbers == more_numbers3)








