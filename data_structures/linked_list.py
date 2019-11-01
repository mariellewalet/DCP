# code to make linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value

class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.tail.next=node
        self.tail = node

    def __contains__(self, node):
        current = self.head
        while current is not None :
            if current is node:
                return True
            current = current.next
        return False

    def __getitem__(self, i):
        counter = 0
        current = self.head
        while current is not None and counter <= i:
            if i == counter:
                return current
            counter+= 1
            current = current.next
        return None

    def __str__(self):
        return_str = ''
        current = self.head
        while current is not None:
            return_str += str(current.value)
            current = current.next
        return return_str

    def __len__(self):
        length = 0
        current = self.head
        while current is not None:
            length+=1
            current = current.next
        return length


if __name__ == '__main__':
    a=Node('a')
    b = Node('b')
    c = Node('c')

    linky = LinkedList(a)
    linky.add(b)
    linky.add(c)
    print(linky[1])
    print(linky)
    print(len(linky))