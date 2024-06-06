class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def insert(self, data):
        if self.data:  # If the node already has data
            if data < self.data:  # If the new data is less, go to the left
                if self.left is None:
                    self.left = Node(data)  # Insert new node if left is empty
                else:
                    self.left.insert(data)  # Recur to the left child
            elif data > self.data:  # If the new data is greater, go to the right
                if self.right is None:
                    self.right = Node(data)  # Insert new node if right is empty
                else:
                    self.right.insert(data)  # Recur to the right child
        else:
            self.data = data  # If the node has no data, set it to the new data

    def print_tree(self):
        if self.left:
            self.left.print_tree()  # Recur to the left child
        print(self.data)  # Print the current node's data
        if self.right:
            self.right.print_tree()  # Recur to the right child

# Creating the binary search tree and inserting data
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

# Printing the tree in in-order traversal
root.print_tree()
