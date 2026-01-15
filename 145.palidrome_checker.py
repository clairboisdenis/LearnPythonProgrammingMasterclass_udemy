def multiply(x, y):
    result = x * y
    return result

print(multiply(50,100))

answer = multiply(40, 20)


print(answer)

for val in range (1, 10):
    result1 = multiply(5, val)
    print(result1)

def is_palindrome(string):
    backwards = string[::-1]
    return backwards == string

print(is_palindrome("backwards"))

def is_palindrome2(varb):
    var1 = varb[::-1]
    return var1 == varb




print(is_palindrome2("massacre"))

mot1 = "magasin"
print(mot1[::])
print(mot1[::2])
print(mot1[::1])

def is_palindrome4():

    word =  input("please, enter you word to detect if it's a palindrome : ")
    print(word[::-1] == word)

is_palindrome4()

def is_palindrome5():
    word = input("please, enter you word to detect if it's a palindrome : ")
    return word == word[::-1]

print(is_palindrome5())

if is_palindrome5():
    print("it's a palindrome")


def is_palindrome6():
    word = input(".6 : "
                 "please, enter you word to detect if it's a palindrome : ")
    return word.casefold() == word[::-1].casefold()

print(is_palindrome6())









