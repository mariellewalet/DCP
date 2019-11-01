""" You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}.
By the pigeonhole principle, there must be a duplicate. Find it in linear time and space."""

def find_duplicate(array):
    dup_count = 0
    count = 0
    for i, value in enumerate(array):
        count += (i+1)
        dup_count += value

    count-= len(array)
    return dup_count-count


if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,9,10,9]
    print(find_duplicate(array))