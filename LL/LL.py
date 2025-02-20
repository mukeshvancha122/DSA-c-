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

    def insertAtEnd(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node

    def insertAtPosition(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
            return
        current = self.head
        count = 0
        while current is not None and count < position - 1:
            current = current.next
            count += 1
        if current is None:
            print("Position out of range")
            return
        new_node.next = current.next
        current.next = new_node
        if new_node.next is None:
            self.tail = new_node

    def printList(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

LL = LinkedList()
LL.insertInBegining(1)
LL.insertInBegining(2)
LL.insertInBegining(3)
LL.insertAtEnd(4)
LL.insertAtPosition(9,2)
print("Nodes in the list:")
LL.printList()
