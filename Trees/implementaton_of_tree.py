class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.rigth = None
    def print_tree(self):
        print(self.data)
root = Node(10)
root.print_tree()