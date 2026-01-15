empty_list = []
even = [2, 4, 6, 8, 10, 12]
odd = [1, 3, 5, 7, 9, 11, 13]

numbers = even + odd
print(type(numbers))
print(numbers)
#numbers.sort()
#print(numbers)

numbers2 = [even, odd]  # 2 list in one
print(numbers2)


for number_list in numbers2:
    print(number_list)
    for value in number_list:
        print(value)
        
