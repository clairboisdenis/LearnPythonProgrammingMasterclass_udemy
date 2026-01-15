import pathlib
from pathlib import Path

split_string = "This string has been\nsplit over\nseveral\nlines"
print(split_string)

tabbedString = "1\t2\t3\t4\t5\t6"
print(tabbedString)

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")
# or
print("""The pet shop owner said "No, no, 'e's uh,...he's resting".""")

# split text with """

anotherSpliString = """This string has
been split
in several lines"""

print(anotherSpliString)

anotherSpliString2 = """This string has \
been yet split \
in several lines \
but with an escape \
character"""

print(anotherSpliString2)

print(r"C:\Users\user1\PycharmProjects\pythonProject1\LearnPythonProgrammingMasterclass")

# print("C:\Users\tom\notes.txt")
# sol1:
print("C:\\Users\\tom\\notes.txt")

# sol2:
print(r"C:\Users\tom\notes.txt")
