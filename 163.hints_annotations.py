def palindrome_sentence(sentence:  str) -> bool:
    """
    Check if a string is a palindrome.

    A palindrome is a string that reads the same forwards as backwards

    :param sentence: The string to check
    :return: True if string is a palindrome, False otherwise
    """
    return sentence.casefold() == sentence[::-1].casefold()


print(palindrome_sentence("ressaser"))

print(palindrome_sentence("ressasser"))

