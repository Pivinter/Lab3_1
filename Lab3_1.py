class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

def print_list(list):
    current_node = list.head
    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next

def split_list(list):
    L1 = DoublyLinkedList()
    L2 = DoublyLinkedList()
    current_node = list.head
    while current_node is not None:
        if current_node.value > 0:
            L1.add_node(current_node.value)
        else:
            L2.add_node(current_node.value)
        current_node = current_node.next
    return L1, L2

L = DoublyLinkedList() #1
L.add_node(1) #2
L.add_node(-2) #3
L.add_node(3) #4
L.add_node(-4) #5
L.add_node(5) #6

print("Початковий список:")
print_list(L)

L1, L2 = split_list(L)

print("Список L1:")
print_list(L1)

print("Список L2:")
print_list(L2)
