"""Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome.
daily should return false, since there's no rearrangement that can form a palindrome."""


def perm_palindrome(string: str):
    # it's a palindrome if and only if,
    #   if the string is of even length then all the characters occur an even number of times
    #   if the string is of odd length then only one character occurs an unever number of times (it'll be the one in the middle)
    set_chars = set(string)
    length = len(string)
    one_odd = False
    for char in set_chars:
        num_occur = string.count(char)
        if num_occur%2 == 1:
            if length%2==1 and not one_odd:
                one_odd= True
            else:
                return False
    return True


if __name__ == '__main__':
    print(perm_palindrome('carrace'))
    print(perm_palindrome('daily'))

