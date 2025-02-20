class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertInBegining(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head=new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def printList(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

LL = LinkedList()
LL.insertInBegining(1)
LL.insertInBegining(2)
LL.insertInBegining(3)

print("Nodes in the list:")
LL.printList()
