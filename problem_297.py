""" At a popular bar, each customer has a set of favorite drinks, and will happily accept any drink among this set.
For example, in the following situation, customer 0 will be satisfied with drinks 0, 1, 3, or 6.

preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}
A lazy bartender working at this bar is trying to reduce his effort by limiting the drink recipes he must memorize.
Given a dictionary input such as the one above, return the fewest number of drinks he must learn in order to satisfy all customers.

For the input above, the answer would be 2, as drinks 1 and 5 will satisfy everyone."""

def subset_list(sub, list):
    temp = False
    for i in list:
        temp = temp or all(elem in i for elem in sub)
    return temp

# barbaric version
def lazy_menu(pref):
    menu = {}
    people = pref.keys()
    for key, value in pref.items():
        for drink in value:
            if drink in menu:
                menu[drink].append(key)
            else:
                menu[drink] = [key]

    # remove all subsets ex: [[0], [0,1]] becomes [[0,1]]
    preferences = [value for value in menu.values()]
    preferences.sort(key = lambda lst: len(lst))
    removed = [value for value in menu.values()]
    for i, value in enumerate(preferences):
        if subset_list(value, preferences[i+1:]):
            removed.remove(value)

    #check which subsets when take the union, it's equal to all of the people
    set_needed  = []
    flat_list = [item for sublist in removed for item in sublist]
    for i in menu.keys():
        if flat_list.count(i) == 1:
            to_change = [item for item in removed if i in item][0]
            set_needed.append(to_change)
            removed.remove(to_change)

    flat_list = [item for sublist in removed for item in sublist]
    print(flat_list)
    print(removed)




if __name__ == '__main__':
    preferences = {
        0: [0, 1, 3, 6],
        1: [1, 4, 7],
        2: [2, 4, 7, 5],
        3: [3, 2, 5],
        4: [5, 8]
    }

    lazy_menu(preferences)
