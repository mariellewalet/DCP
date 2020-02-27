"""This problem was asked by Glassdoor.

An imminent hurricane threatens the coastal town of Codeville.
If at most two people can fit in a rescue boat, and the maximum weight limit for a given boat is k,
determine how many boats will be needed to save everyone.

For example, given a population with weights [100, 200, 150, 80] and a boat limit of 200,
the smallest number of boats required will be three."""


def number_boats(limit, population):
    k=0

    #remove all of the basic cases (for example if someone's weight is the limit, can't add more)
    min_weight = min(population)

    for person in population:
        if limit-person<min_weight:
            population.remove(person)
            k+=1

    while population:
        max_weight = max(population)
        min_weight = min(population)

        if max_weight+min_weight<= limit:
            population.remove(max_weight)
            population.remove(min_weight)
            k+=1
        else:
            population.remove(max_weight)
            k+=1

    return k


if __name__ == '__main__':
    print(number_boats(200, [100,200,150,80]))