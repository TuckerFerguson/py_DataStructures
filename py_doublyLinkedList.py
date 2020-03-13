"""
@author Tucker Ferguson
3/7/2020

@description 

This is an implementation of a doubly linked list written in python

"""

#Container for data, individual element of list
class node:
    def __init__(self,dataval):
        self.dataval = dataval
        self.nextval = None
        self.prevval = None

#Creates doubly linked list, consisting of nodes       
class dLinkedList:
    def __init__(self):
        self.head = None

#adds node to end of list    
    def append(self, dataval):
        newNode = node(dataval.dataval)
        if(self.head is None):
            self.head = newNode
            return
        
        lastnode = self.head
        while(lastnode.nextval is not None):
            lastnode = lastnode.nextval
        lastnode.nextval = newNode
        newNode.prevval = lastnode

#insert new node at specified location (prevval)
    def insert(self,prevval,dataval):
        if(self.head is None):
            print("empty list")
            return 
        
        newNode = node(dataval.dataval)
        
        newNode.nextval = prevval.nextval
        prevval.nextval = newNode
        newNode.prevval = prevval

#removes specified (by value) node 
    def remove(self,dataval):
        
        newNode = node(dataval.dataval)
        head = self.head
        
        while(head.nextval is not None):
            if(head.dataval == newNode.dataval):
                head.prevval.nextval = head.nextval
                head.nextval.prevval = head.prevval
                return 
            head = head.nextval

#prints each element of the DLL
    def printList(self,node):
        while(node is not None):
            print(node.dataval)
            dummy = node
            node = dummy.nextval

#Create double linked list object
mylist = dLinkedList()

#Create nodes
A = node("node: A")
B = node("node: B")
C = node("node: C")
D = node("node: D")


#Populate our list with nodes
mylist.append(A)
mylist.append(B)
mylist.append(C)
mylist.append(D)


#Print our list
#mylist.printList(mylist.head)

#Insert Check
print("""insert() method demo: ABCD -> AA2BCD""")
A2 = node("node: A2")
mylist.insert(mylist.head,A2)
mylist.printList(mylist.head)

#Remove Check
print("""\nremove() method demo: AA2BCD -> ABCD""")
mylist.remove(A2)
mylist.printList(mylist.head)
