"""Implement a 2D iterator class. It will be initialized with an array of arrays,
and should implement the following methods:

next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
has_next(): returns whether or not the iterator still has elements left.
For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty."""

class twoD:
    def __init__(self,array):
        self.array = array
        self.first, self.second = -1,-1
        self.first, self.second = self.find_next_index()

    def find_next_index(self):
        first = self.first
        second = self.second
        if first == -1 and second == -1:
            first, second= 0,0
        else:
            second += 1

        if second<len(array[first]):
            return first, second

        for i in range(first+1, len(self.array)):
            if 0 == len(array[i]):
                continue
            if 0 < len(array[i]):
                return i, 0
        return -1,0

    def has_next(self):
        if self.find_next_index() == (-1,0):
            return False
        return True

    def next(self):
        if self.first == -1:
            raise Exception('No more elements left')
        to_print = self.array[self.first][self.second]
        self.first, self.second = self.find_next_index()
        return to_print


if __name__=='__main__':
    array = [[1, 2], [3], [], [4, 5, 6]]
    iterator = twoD(array)

    while iterator.has_next():
        print(iterator.next())
    print(iterator.next())
