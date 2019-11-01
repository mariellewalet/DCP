""" Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, replace the color of the given pixel and all adjacent same colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

B B W
W W W
W W W
B B B
Becomes

B B G
G G G
G G G
B B B """

""" we are going to use an alternate BFS in order to traverse all of the pixels with a certain color"""

def replace_color(matrix: list, loc: tuple, new_colour: str):
    # check if the location is valid
    # location is of the form : row, column
    if loc[0]>=len(matrix) or loc[1]>=len(matrix[0]):
        return matrix

    old_colour = matrix[loc[0]][loc[1]]

    if old_colour == new_colour:
        return matrix

    to_visit = set()
    to_visit.add(loc)

    while to_visit:
        coord = to_visit.pop()
        matrix[coord[0]][coord[1]] = new_colour

        if coord[0]>0 and matrix[coord[0]-1][coord[1]] == old_colour:
            to_visit.add((coord[0]-1, coord[1]))

        if coord[0]<len(matrix)-1 and matrix[coord[0]+1][coord[1]] == old_colour:
            to_visit.add((coord[0]+1, coord[1]))

        if coord[1]>0 and matrix[coord[0]][coord[1]-1] == old_colour:
            to_visit.add((coord[0], coord[1]-1))

        if coord[1]<len(matrix[0])-1 and matrix[coord[0]][coord[1]+1] == old_colour:
            to_visit.add((coord[0], coord[1]+1))

    return matrix


if __name__ == '__main__':
    matrix = [
        ['B', 'B', 'W'],
        ['W', 'W', 'W'],
        ['W', 'W', 'W'],
        ['B', 'B', 'B']
    ]

    print(replace_color(matrix, (2,2), 'G'))