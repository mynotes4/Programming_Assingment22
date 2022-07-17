"""
Question5
Create a function that takes a string and returns True or False, depending on whether the
characters are in order or not.
Examples
is_in_order("abc") ➞ True
is_in_order("edabit") ➞ False
is_in_order("123") ➞ True
is_in_order("xyzz") ➞ True
Notes
You don't have to handle empty strings.
"""

def is_in_order(s):
    if s == ''.join(sorted(s)):
        return True
    return False

s = input("Enter word ")
print("is_isogram(",s,") ➞",is_in_order(s))