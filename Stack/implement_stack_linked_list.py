class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class stack:
    def __init__(self) -> None:
        self.head = None
        
    def is_empty(self):
        if self.head== None:
            return True
        else:
            print("stack is not empty")
            return False
    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            
    def pop(self):
        if self.is_empty():
            return  None
        else:
            pop_node = self.head
            self.head= self.head.next
            pop_node.next = None
            return pop_node.data
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data
    def display(self):
        temp = self.head
        if self.is_empty():
            return None
        else:
            while temp:
                print(temp.data,end = " ")
                temp = temp.next
                if temp!= None:
                    print("->",end = " ")
            return
if __name__ == "__main__":
    MyStack = stack()
   
    MyStack.push(11)
    MyStack.push(22)
    MyStack.push(33)
    MyStack.push(44)
 
  # Display stack elements
    MyStack.display()
 
  # Print top element of stack
    print("\nTop element is ", MyStack.peek())
 
  # Delete top elements of stack
    MyStack.pop()
    MyStack.pop()
 
  # Display stack elements
    MyStack.display()
 
  # Print top element of stack
    print("\nTop element is ", MyStack.peek())