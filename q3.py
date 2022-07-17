"""
Question3
A group of friends have decided to start a secret society. The name will be the first letter of
each of their names, sorted in alphabetical order.
Create a function that takes in a list of names and returns the name of the secret society.
Examples
society_name(["Adam", "Sarah", "Malcolm"]) ➞ "AMS"
society_name(["Harry", "Newt", "Luna", "Cho"]) ➞ "CHLN"
society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"])
"""
def society_name(s):
    s = str_list(s)
    s1 = ''
    for i in s:
        s1 = s1 + i[0]
    return ''.join(sorted(s1))

def str_list(s):
    s = s.split(' ')
    return [i for i in s]

s = input("Enter names in following form\n a b c : ")
sn = society_name(s)
print("society_name([",str_list(s),") ➞",sn)