from data_structures.linked_list import Node, LinkedList

"""Given a linked list and a positive integer k, rotate the list to the right by k places.

For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.

Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2."""


def rotate(linked, k):
    length_linked = len(linked)

    if length_linked<= 1:
        return linked

    while length_linked<=k:
        k -= length_linked

    if k == 0:
        return linked

    original_head = linked.head
    new_head = linked[k]
    original_tail = linked.tail
    new_tail = linked[(k-1)%length_linked]

    linked.head = new_head
    original_tail.next = original_head
    new_tail.next = None
    linked.tail = new_tail

    return linked


if __name__ == '__main__':
    a=Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')

    linky = LinkedList(a)
    linky.add(b)
    linky.add(c)
    linky.add(d)
    linky.add(e)

    print(rotate(linky, 3))