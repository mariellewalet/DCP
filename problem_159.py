""" Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
"""


def is_recurring(s: str):
    seen_chars = set()
    for i in s:
        if i in seen_chars:
            return i
        seen_chars.add(i)


if __name__ == '__main__':
    print(is_recurring('acbbac'))
    print(is_recurring('abcdef'))