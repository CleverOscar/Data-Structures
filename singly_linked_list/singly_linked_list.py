class Node:
    # Constructor
    def __init__(self, data,next=None):
        self.data = data
        self.next = next

    def has_value(self, data):
        if self.data == data:
            return True
        else:
            return False


#Uncomment to create a single node
first = Node(3)
print(first.data)
print(first.has_value(3))


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        newNode = Node(data)

        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def add_to_head(self, data):

        if self.head > 0:
            self.head = data[0]
        else:
            self.head.data = data





'''
    Uncomment to see Linked List with Single Node
    LL = LinkedList()
    LL.head = Node(3)
 print(LL.head.data)
'''
