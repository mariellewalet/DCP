"""
Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the
string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must
remove all of them.
"""


def num_remove(string):
    temp = 0
    to_remove = 0
    for char in string:
        if char == '(':
            temp += 1
        if char == ')':
            temp -= 1
        if temp < 0:
            temp += 1
            to_remove += 1
    return to_remove + temp


# should print 1
print(num_remove("()())()"))
# should print 2
print(num_remove(")("))
