

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        new_node=Node(data)
        if self.top is None:
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node
    def print(self):
        current=self.top
        while current:
            print("data in stack: ", current.data)
            current=current.next 

    def pop(self):
        if self.top is None:
            print("No items in the list")
            return None
        else:
            popped_data=self.top.data
            self.top=self.top.next
            return popped_data
        
stack1=Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.pop()
stack1.print()
