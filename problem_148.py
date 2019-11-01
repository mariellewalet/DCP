""" Gray code is a binary code where each successive value differ in only one bit, as well as when wrapping around.
Gray code is common in hardware so that we don't see temporary spurious values during transitions.

Given a number of bits n, generate a possible gray code for it.

For example, for n = 2, one gray code would be [00, 01, 11, 10]."""


def gray_code(n: int):
    if n <= 0:
        return None

    gray = ['0', '1']

    if n == 1:
        return gray

    for j in range(2,n+1):
        first_part = gray
        second_part = gray[::-1]

        for i, _ in enumerate(gray):
            first_part[i]  = '0'+first_part[i]
            second_part[i] = '1'+second_part[i]

        gray = first_part+second_part
    return gray


if __name__ == '__main__':
    print(gray_code(4))