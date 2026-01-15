def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return string.casefold() == string[::-1].casefold()


print(palindrome_sentence("Hello I am a curious guy"))

word =  "ressasser"
if palindrome_sentence(word):
    print("{} is a palinbdrome.".format(word))
else:
    print("{} is not a palindrome.".format(word))

word = "tremendious"

for i in range(len(word)):

    print(i)

for i in range (0,10):
    print(i)
    

