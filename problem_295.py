""" Pascal's triangle is a triangular array of integers constructed with the following formula:

The first row consists of the number 1.
For each subsequent row, each element is the sum of the numbers directly above it, on either side.
For example, here are the first few rows:"""


def barbaric_pascal(k):
    if k < 1:
        return None
    current = [1]

    if k == 1:
        return current

    counter = 2
    next = [1,1]

    while counter <= k:
        current = next
        next = [1]
        for i in range(counter-1):
            next.append(current[i]+current[i+1])
        next.append(1)
        counter += 1

    return current


if '__main__' == __name__:
    print(barbaric_pascal(5))