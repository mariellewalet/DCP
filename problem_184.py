""" Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14."""


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def gcd_array(arr: list):
    i = 0
    result = arr[0]

    while i < len(arr):
        result = gcd(result, arr[i])
        i += 1
    return result


if __name__ == '__main__':
    array = [42,56,13]
    print(gcd_array(array))


