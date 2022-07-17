"""
Question2
Create a function that takes in two lists and returns True if the second list follows the
first list by one element, and False otherwise. In other words, determine if the second list
is the first list shifted to the right by 1.
Examples
simon_says([1, 2], [5, 1]) ➞ True
simon_says([1, 2], [5, 5]) ➞ False
simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]) ➞ True
simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]) ➞ False
Notes
Both input lists will be of the same length, and will have a minimum length of 2.
The values of the 0-indexed element in the second list and the n-1th indexed element in the
first list do not matter.
"""
def simon_says(l1,l2):
    if len(l1) < 2 or len(l2) < 2:
        return "Minimum length of list should be 2"
    if len(l1) != len(l2):
        return "Both list should be of same length"
    l1 = str_list(l1)
    l2 = str_list(l2)
    for i in range(len(l1)-1):
        if l1[i] != l2[i+1]:
            return False
    return True

def str_list(l):
    l = l.split(' ')
    l1 = [int(i) for i in l]
    return l1

l1 = input("Enter list 1 in following form\n1 2 3 4: ")
l2 = input("Enter list 2 in following form\n1 2 3 4: ")
print("simon_says(",l1,",",l2,") ➞,",simon_says(l1,l2))