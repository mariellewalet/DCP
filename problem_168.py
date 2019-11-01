""" Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
you should return:

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
"""


# with extra space
def rotate(matrix):
    n = len(matrix)
    rotated = []
    for column in range(0,n):
        new_row = []
        for row in range(n-1,-1, -1):
            new_row.append(matrix[row][column])
        rotated.append(new_row)
    return rotated


if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    print(rotate(matrix))