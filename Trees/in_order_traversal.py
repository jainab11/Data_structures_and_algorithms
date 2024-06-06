class Node:
    def __init__(self,data) :
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()
    def in_order(self,root):
        # left->root->-right
        res =[]
        if root:
            res = self.in_order(root.left)
            res.append(root.data)
            res = res+self.in_order(root.right)
        return res
    
root = Node(27)
root.insert(12)
root.insert(16)
root.insert(19)
root.insert(22)
root.insert(56)
root.insert(67)
root.insert(98)
print(root.in_order(root))


        