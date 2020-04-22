from doubly_linked_list import DoublyLinkedList
# import sys
# sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size == 0:
            return
        self.size -= 1
        return self.storage.remove_from_tail()

    def len(self):
        return self.size