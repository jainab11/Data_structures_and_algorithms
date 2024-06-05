class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class queue:
    def __init__(self) :
        self.front = self.rear = None
    def is_empty(self):
        if self.front and self.rear == None:
            return True
        return False
    #  add item to queue
    def EnQueue(self,data):
        temp = Node(data)
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp
    def DeQueue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = temp.next
        if(self.front == None):
            self.rear = None

if __name__ == '__main__':
    q = queue()
    q.EnQueue(10)
    q.EnQueue(20)
    q.DeQueue()
    q.DeQueue()
    q.EnQueue(30)
    q.EnQueue(40)
    q.EnQueue(50)
    q.DeQueue()
    print("Queue Front : " + str(q.front.data if q.front != None else -1))
    print("Queue Rear : " + str(q.rear.data if q.rear != None else -1))
        
            