""" A girl is walking along an apple orchard with a bag in each hand.
She likes to pick apples from each tree as she goes along,
but is meticulous about not putting different kinds of apples in the same bag.

Given an input describing the types of apples she will pass on her path, in order,
determine the length of the longest portion of her path that consists of just two types of apple trees.

For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3,
with a length of four."""

def longest_path_apples(path):
    type1= path[0]
    start1 = 0
    type2 = None
    start2 = -1
    max_len = -1
    end = -1
    while start1 <len(path):
        for i in range(start1, len(path)):
            if path[i] == type1:
                continue
            else:
                type2 = path[i]
                start2 = i
                break

        if start2 == -1 :
            break

        for i in range(start2, len(path)):
            if path[i] == type1 or path[i] == type2:
                continue
            else:
                end = i
                break
        max_len = max(max_len, end-start1)
        start1 = start2
        type1 = type2

    if max_len == -1:
        return len(path)
    return max_len


if __name__ == '__main__':
    path = [2, 1, 2, 3, 3, 1, 3, 5]
    print(longest_path_apples(path))