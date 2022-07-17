"""Question4
An isogram is a word that has no duplicate letters. Create a function that takes a string and
returns either True or False depending on whether or not it's an "isogram".
Examples
is_isogram("Algorism") ➞ True
is_isogram("PasSword") ➞ False
# Not case sensitive.
is_isogram("Consecutive") ➞ False
Notes
Ignore letter case (should not be case sensitive).
All test cases contain valid one word strings.
"""

def is_isogram(s):
    char = []
    for i in s:
        if chr(ord(i)) in char or chr(ord(i) + 32) in char:
            return False
        else:
            char.append(i)
    return True

s = input("Enter word ")
print("is_isogram(",s,") ➞",is_isogram(s))
