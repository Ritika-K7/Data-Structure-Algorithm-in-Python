""" Singly Linked List"""

class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start
    
    def is_empty(self):
        return self.start==None

    def  insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n

    def insert_at_last(self,data):
        n=Node(data)    
        if not self.is_empty():
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=n    
        else:
            self.start=n
    
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n

    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')


#Driver Code
mylist=SLL()       
