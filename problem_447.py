""" Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024. """
import math


def pow(num, exp):
    if exp == 0:
        return 1
    acc = 1
    while exp >1:
        if exp%2 == 1:
            acc *= num
            exp -= 1
        exp /=2
        num *= num
    return acc*num


if __name__ == '__main__':
    print(pow(2, 10))
