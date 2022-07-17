"""
Question1
Create a function that takes three parameters where:
x is the start of the range (inclusive).
y is the end of the range (inclusive).
n is the divisor to be checked against.
Return an ordered list with numbers in the range that are divisible by the third parameter
n. Return an empty list if there are no numbers that are divisible by n.
Examples
list_operation(1, 10, 3) ➞ [3, 6, 9]
list_operation(7, 9, 2) ➞ [8]
list_operation(15, 20, 7) ➞ []
"""

def list_operation(x,y,n):
    l = [i for i in range(x,y+1) if i % n == 0 ]
    return  l

x = int(input("Enter the start of the range (inclusive). "))
y = int(input("Enter is the end of the range (inclusive). "))
n = int(input("n is the divisor to be checked against. "))
l = list_operation(x,y,n)
print("list_operation(",x,",",y,",",n,") ➞",l)