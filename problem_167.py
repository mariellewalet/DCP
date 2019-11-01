""" Given a list of words, find all pairs of unique indices
such that the concatenation of the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)] """


def palindrome(words: list):
    solution = []
    for i, first in enumerate(words):
        for j, second in enumerate(words):
            if i==j:
                continue
            concat = first+second
            if concat == concat[::-1]:
                solution.append((i,j))
    return solution


if __name__ == '__main__':
    words = ["code", "edoc", "da", "d"]
    print(palindrome(words))
