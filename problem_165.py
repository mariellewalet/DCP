"""Given an array of integers, return a new array where each element in the new array is
the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1"""

def problem(array):
    solution = []
    for i in range(0, len(array)):
        solution.append(find_smaller(array, i))
    return solution

def find_smaller(array, index):
    counter = 0
    for i in range(index+1, len(array)):
        if array[i]<array[index]:
            counter+=1
    return counter


if __name__ == '__main__':
    array = [3,4,9,6,1]
    print(problem(array))