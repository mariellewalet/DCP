"""This problem was asked by Facebook.

On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue.
One power of the Qux is that if two of them are standing next to each other,
they can transform into a single creature of the third color.

Given N Quxes standing in a line,
determine the smallest number of them remaining after any possible sequence of such transformations.

For example, given the input ['R', 'G', 'B', 'G', 'B'],
it is possible to end up with a single Qux through the following steps:

        Arrangement       |   Change
----------------------------------------
['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
['B', 'B', 'G', 'B']      | (B, G) -> R
['B', 'R', 'B']           | (R, B) -> G
['B', 'G']                | (B, G) -> R
['R']                     |"""


def possible_changes(quxes):
    changes = []
    for i in range(len(quxes)-1):
        if quxes[i] != quxes[i+1]:
            element = quxes[i]
            changes.append(quxes.pop(i))
            quxes.insert(i, element)

            element = quxes[i+1]
            changes.append(quxes.pop(i+1))
            quxes.insert(i+1, element)
    return changes


def remove_quxes(quxes):
    changes = possible_changes(quxes)
    if not changes :
        return len(quxes)
    else:
        min_step = 10000
        for new_quxes in changes:
            min_step = min(min_step, remove_quxes(new_quxes))
            return min_step


if __name__ =='__main__':
    print(remove_quxes(['R', 'G', 'B', 'G', 'B']))
