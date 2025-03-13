class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val=val 
        self.left=left 
        self.right=right 

    def __str__(self):
        return str(self.val)

    def inorder(self,node):
        if not node:
            return 
        self.inorder(node.left)
        print(node)
        self.inorder(node.right)

    def postorder(self,node):
        if not node:
            return  
        self.preorder(node.left)
        self.preorder(node.right)
        print(node) 
    

    def preorder(self, node):
        if not node:
            return  
        print(node)
        self.preorder(node.left)
        self.preorder(node.right)

A= TreeNode(1) 
B= TreeNode(2) 
C= TreeNode(3) 
D= TreeNode(4) 
E= TreeNode(5) 
F= TreeNode(10) 

A.left=B 
A.right=C 
B.right=D 
B.left=E 
C.left=F 

print("Inorder Traversal:")
A.inorder(A)
print("\nPostorder Traversal:")
A.postorder(A)
print("\nPreorder Traversal:")
A.preorder(A)


