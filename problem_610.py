"""
Implement division of two positive integers without using the division, multiplication, or modulus operators.
Return the quotient as an integer, ignoring the remainder.
"""

def division(a: int, b: int) -> int:

    if a<b:
        return 0
    if a == b:
        return 1
    quotient = 0
    while a > b:
        a -= b
        quotient += 1
    return quotient

