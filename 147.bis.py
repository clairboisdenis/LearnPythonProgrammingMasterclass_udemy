
def palindrome_sentence(sentence):
    return sentence.casefold() == sentence[::-1].casefold()


print(palindrome_sentence("ressaser"))

print(palindrome_sentence("ressasseer"))

