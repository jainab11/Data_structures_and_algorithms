'''
@Author: Author Name
@Date: 2021-02-11 18:00:30
@Last Modified by: Author Name
@Last Modified time: 2021-02-11 18:00:30
@Title : Implemention of stack data structure
'''
# satck is  linear data structure  first in last out or last in first out LIFO
""" Stack real lif application is 
Undo/redo functionality:
Backtracking algorithms:
Function calls:

To implement the stack operations, 
you need to use the push, pop, peek, isEmpty, and isFull methods
"""
from sys import maxsize
#  stack creation using array or list
def create_stack():
    stack = []
    return stack

#  code for is dtck is empty
def is_empty(stack):
    return len(stack)==0

# to add item in stack
def push(stack,item):
    stack.append(item)
    print(f"{item} pushed to stack")

# removing top element from stack

def pop_item(stack):
    if(is_empty(stack)):
        return str(-maxsize -1)
    return stack.pop()

# print elemnt at top of stack
def peek(stack):
    if(is_empty(stack)):
        return str(-maxsize -1)
    return stack[len(stack)-1]
#  because last element of stack at top
        
stacks = create_stack()
# push(stacks,str(10))
# push(stacks,str(23))
# push(stacks,str(38))
# push(stacks,str(34))
print(pop_item(stacks)+ " Top element removed")
print(peek(stacks) + " Peek element ")
print("Present element in stack "+ str(stacks))