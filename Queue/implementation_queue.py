""" There a two way to implement queue
1.using list
2. using deque"""
que = []
que.append(1)
que.append(2)
que.append(3)
que.append(4)
print(f"queue after adding elemnt {que}")
print(que.pop(0))
print(que.pop(0))
print(que.pop(0))
print(que.pop(0))
print("\nQueue after removing elements")
print(que)
 
from collections import deque
q = deque()
q.append("a")
q.append("b")
q.append("c")
print("queue")
print(q)
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q)
