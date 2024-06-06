class Stack:
    def __init__(self) :
        self.stack = []
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("empty stack")
    def push(self,item):
        self.stack.append(item)
    
    def peek(self):
        if self.is_empty():
            return(self.stack[-1])
        else:
            raise IndexError("stack empty")
        
    
    def size(self):
        return(len(self.stack))
    
    def __str__(self):
        return str(self.stack)
    
def bubble_sort(stack):
    n = stack.size()
    temp = []  # Initialize temp outside the outer loop
    for i in range(n):
        for j in range(0, n - i - 1):
            top1 = stack.pop()
            top2 = stack.pop()
            if top1 > top2:
                temp.append(top1)  
                stack.push(top2)
            else:
                temp.append(top2)
                stack.push(top1)
        # Place the sorted elements at the bottom of the stack
        for _ in range(n - i - 1):
            stack.push(temp.pop())
    return stack
stack = Stack()
elements = [3, 1, 4, 2]
for element in elements:
    stack.push(element)

print("Original stack:", stack)
sorted_stack = bubble_sort(stack)
print("Sorted stack:  ", sorted_stack)