""" Given a start word, an end word, and a dictionary of valid words, find the shortest transformation sequence from
start to end such that only one letter is changed at each step of the sequence, and each transformed word exists in the
dictionary. If there is no possible transformation, return null. Each word in the dictionary have the same length as
start and end and is lowercase.

For example, given start = "dog", end = "cat", and dictionary = {"dot", "dop", "dat", "cat"},
return ["dog", "dot", "dat", "cat"].

Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"},
return null as there is no possible transformation from dog to cat.
"""

#   General idea :
#   Make this problem into a graph problem. Node = Word. Connect two nodes if they are one letter
#   change apart

import queue

class Node():
    def __init__(self, word, isStart = False, isEnd = False):
        self.word = word
        self.neigh = set()
        self.start = isStart
        self.end = isEnd

    def isStart(self):
        return self.start

    def isEnd(self):
        return self.end

    def isNeighbour(self, node):
        diff = False
        for i, letter in enumerate(self.word):
            if letter != node.word[i]:
                if diff:
                    return False
                diff = True
        return diff

    def addNeighbours(self, neighbours):
        for neigh in neighbours:
            if self.isNeighbour(neigh):
                self.neigh.add(neigh)


def dijkstra(start, end, nodes):
    distance = {node: 1000 for node in nodes}
    distance[start] = 0
    parent = {node:None for node in nodes}
    priority = []

    def add_priority_queue(node):
        priority.append((distance[node], node))
        priority.sort(key=lambda a: a[0], reverse=True)

    add_priority_queue(start)

    while len(priority)>0:
        dist, node = priority.pop(0)


        for neigh in node.neigh:
            if 1+dist < distance[neigh]:
                distance[neigh] = 1+dist
                parent[neigh] = node
                add_priority_queue(neigh)

        if node == end:
            sequence = [end.word]
            node = parent[end]
            while node != start:
                sequence.insert(0, node.word)
                node = parent[node]
            sequence.insert(0, node.word)
            return sequence




def find_shortest_seq( start_word, end_word, dictionary):
    nodes = []
    start = None
    end = None
    for word in dictionary:
        if word == start_word:
            start = Node(word, isStart=True)
            nodes.append(start)
        elif word == end_word:
            end = Node(word, isEnd=True)
            nodes.append(end)
        else:
            temp = Node(word)
            nodes.append(temp)

    if start is None:
        start = Node(start_word, isStart=True)
        nodes.append(start)

    if end is None:
        print("Not possible")
        return

    for node in nodes:
        node.addNeighbours(nodes)

    print(dijkstra(start, end, nodes))


start = "dog"
end = "cat"
dictionary = {"dot", "tod", "dat", "dar"}
find_shortest_seq(start, end, dictionary)






