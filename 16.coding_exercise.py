t = input("enter a word : ")
n = int(input("Give a number : "))

def sum_eo(n, t):
    sum = 0
    if t == 'e':
        for i in range(n + 1):
            if i % 2 == 0:
                sum += i
        return sum
    elif t == "o":
        for i in range(n + 1):
            if i % 2 == 1:
                sum += i
        return sum
    else:
        return -1


x = sum_eo(n, t)
print(f"the sum is {x} ")


