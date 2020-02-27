""" You are given a list of (website, user) pairs that represent users visiting websites.
Come up with a program that identifies the top k pairs of websites with the greatest similarity.

For example, suppose k = 1, and the list of tuples is:

[('a', 1), ('a', 3), ('a', 5),
 ('b', 2), ('b', 6),
 ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5)
 ('d', 4), ('d', 5), ('d', 6), ('d', 7),
 ('e', 1), ('e', 3), ('e': 5), ('e', 6)]
Then a reasonable similarity metric would most likely conclude that a and e are the most similar,
so your program should return [('a', 'e')]."""


def similarity(k, lst):
    website_user = {}
    for (website, user) in lst :
        if website in website_user:
            website_user[website].append(user)
        else:
            website_user[website] = [user]

    def function(a,b):
        similar = 0
        for users_a in website_user[a]:
            for users_b in website_user[b]:
                if users_a == users_b:
                    similar+= 1

        return similar/max(len(website_user[a]), len(website_user[b]))

    similar_lst = []
    for i, a in enumerate(website_user.keys()):
        for j, b in enumerate(website_user.keys()):
            if a!=b and i<j:
                similar_lst.append(((a,b),function(a, b)))

    similar_lst.sort(reverse=True, key = lambda tup: tup[1])
    print(similar_lst)
    return [tup[0] for tup in similar_lst][0:k]


if __name__ == '__main__':
    lst = [('a', 1), ('a', 3), ('a', 5),
           ('b', 2), ('b', 6),
           ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
           ('d', 4), ('d', 5), ('d', 6), ('d', 7),
           ('e', 1), ('e', 3), ('e', 5), ('e', 6)]
    print(similarity(2, lst))

