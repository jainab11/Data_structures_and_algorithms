class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self,head = None):
        self.head = head
    
    def insert_at_begning(self,data):
        """ This function is for inserting element at begning of linked list

        Args:
            data (int): it a data value which is going to be insert in the linked list
        """
        node = Node(data,self.head)
        self.head = node
        
    def display(self):
        """This function is to print linked list as well as travers in linked list  """
        if self.head is None:
            print("Empty")
            return
        #  creating a temp variable so the original will not change
        temp = self.head
        data_val = ''
        while temp:
            # this is to add element in data_val
            data_val += str(temp.data) + "->"
            # to go to next element store make temp to point temp next
            temp = temp.next
        print(data_val)
    def get_length(Self):
        count =0 
        temp = Self.head
        while temp:
            count+=1
            temp = temp.next
        return count
    
    def insert_at_end(self,data):
        # if linke list in empty
        if self.head is None:
            #add element at the and make  next as None
            self.head = Node(data,None)
            return
        # if linked list is not blank
        temp = self.head
        while temp.next:
            # go to last element of linked list
            temp = temp.next
        temp.next = Node(data,None)
        
    def inser_values(self,lst):
        self.head = None
        for data in lst:
            self.insert_at_end(data)
    def remove_at_index(self,ind):
        
        if ind <0  or ind >=self.get_length():
            raise Exception("index is not valid")
        if ind == 0:
            self.head == self.head.next
            return
        count = 0 
        temp = self.head
        while temp:
            if count == ind-1:
                temp.next = temp.next.next
                break
            temp = temp.next
            count +=1
        
    def insrt_at_index(self,ind,data):
        if ind <0  or ind >=self.get_length():
            raise Exception("index is not valid")
        
        if ind == 0:
            self.insert_at_begning(data)
        count = 0
        temp = self.head
        while temp:
            if count == ind -1:
                node = Node(data,temp.next)
                temp.next = node
                break
            temp = temp.next
            count +=1
    def remove_at_values(self,data):
        if self.heat is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        temp = self.head
        while temp:
            if temp.next.data == data:
                temp.next = temp.next.next
                break
            temp = temp.next
    def inser_after_values(self,data):
        pass

if __name__ == '__main__':
    ll = LinkedList()
    ll.inser_values(["a","b","C"])
    ll.insrt_at_index(2,"d")
    ll.remove_at_index(1)

    ll.display()
    print(ll.get_length(),"length of ll")
    