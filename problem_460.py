"""Good morning! Here's your coding interview problem for today.

This problem was asked by LinkedIn.

You are given a string consisting of the letters x and y, such as xyxxxyxyy.
In addition, you have an operation called flip, which changes a single x to y or vice versa.

Determine how many times you would need to apply this operation to ensure that all x's come before all y's.
In the preceding example, it suffices to flip the second and sixth characters, so you should return 2."""

#basic thing - i know it's wrong
def num_flips_needed(string):
    i = string.len()-1
    x_encountered = False

    for i in range(i,-1, -1):
        if x_encountered:
            pass


def num_flips_version2(string: str):
    num_flips = 0
    #remove the edge cases
    if 'x' not in string:
        return 0
    if 'y' not in string:
        return 0

    x_encountered = False
    start_index = -1
    for i in range(len(string)-1, -1, -1):
        if x_encountered and string[i] == 'y':
            start_index = i
            break
        if string[i] == 'x':
            x_encountered = True

    if start_index == -1:
        return 0

    #Now that we have removed all edge cases, need to do all of the calculations
    def rec_func(x_portion: bool, sub: str, acc: int):
        if len(sub) == 0:
            return acc
        for j in range(string.len()-1, -1, -1):
            if not x_portion and sub[j] == 'x':
                return min(rec_func(True, sub[:j], acc), rec_func(False, sub[:j], acc+1))
            if x_portion and sub[j] == 'y':
                return rec_func(True, sub[:j], acc+1)
        return acc

    return min(rec_func(False, str[:i], 1), rec_func(True, str[:i], 0))


if __name__ == '__main__':
    print(num_flips_version2('xyx'))
