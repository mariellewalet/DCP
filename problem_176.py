""" Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters. """


def one_to_one(str1, str2):
    # a on
    length_str = len(str1)
    set1 = set(str1)
    set2 = set(str2)

    if len(set1) >= len(set2):
        return True

    return False

if __name__ == '__main__':
    print(one_to_one('abc', 'bdc'))
    print(one_to_one('foo', 'bar'))