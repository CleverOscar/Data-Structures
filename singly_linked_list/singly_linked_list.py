class Node:
    # Constructor
    def __init__(self, data,next=None):
        self.data = data
        self.next = next


#Uncomment to create a single node
# first = Node(3)
# print(first.data)


class LinkedList:
    def __init__(self):
        self.head = None


#Uncomment to see Linked List with Single Node
# LL = LinkedList()
# LL.head = Node(3)
# print(LL.head.data)
