class ListNode:
    # Constructor
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next



class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = ListNode(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if self.head is None and self.tail is None:
            return
        # what is we only have a single elem in the LinkedList?
        # both head and tail are pointing at the same Node
        if not self.head.get_next():
            self.head = self.head
            # delete the linked list head reference
            self.head = None
            # also need to delete tail reference
            self.tail = None
            return self.head.get_value()

        val = self.head.get_value()
        # set self.head to the Node after the head
        self.head = self.head.get_next()
        return val

    def remove_tail(self):
        if self.head is None and self.tail is None:
            return None

        current = self.head
        while current.get_next() is not self.tail:
            current = current.get_next()
        # at this point current is the node

        self.tail = None

        self.tail = current

    def get_max(self):
        

# linkedlist = ListNode(1)
# print(linkedlist.data)
# linkedlist.set_next(ListNode(2))
# print(linkedlist.next.data)
# linkedlist.next.set_next(ListNode(3))
# print(linkedlist.next.next.data)
# print(linkedlist.next.next.next)
