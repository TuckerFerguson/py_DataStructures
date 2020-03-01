"""
@author Tucker Ferguson
2/17/2020
Description: Pythons adaptation for linked lists, Days of the week
Part2) added print, insertion, and removal methods
"""

#In order to make linked lists possible we must utilize nodes
class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None
        
#Next we need to create our singly linked list class
class sLinkedList :
    def __init__(self):
        self.headval = None;
        
    def printList(self):
        tempVal = self.headval
        while(tempVal is not None):
            try :
                print(tempVal.dataval)
                tempVal = tempVal.nextval
            except AttributeError:
                return
    
    def insertBeginning(self, newData):
        newNode = Node(newData)
        if(self.headval == None):
            self.headval = newNode
        newNode.nextval = self.headval
        self.headval = newNode
    
    def insertEnd(self, newData):
        newNode = Node(newData)
        if(self.headval == None):
            self.headval = newNode
            return
        value = self.headval
        while(value.nextval):
            value = value.nextval
        value.nextval = newNode
    
    def insertMiddle(self,middleNode,newData):
        if(middleNode == None):
            print("Desired node non-existant")
        newNode = Node(newData)
        newNode.nextval = middleNode.nextval
        middleNode.nextval = newNode
    
    def remove(self,key):
        start = self.headval
        if(start == None):
            print("Empty List, nothing to remove")
            return
        if(start is not None):
            if(start.dataval == key):
                self.headval = start.nextval
                start = None
                return
        while(start is not None):
            if(start.dataval == key):
                break;
            prev = start
            start = start.nextval
        prev.nextval = start.nextval
        start = None
    
            
    
    


sl_List = sLinkedList()

#First lets create our headnode
sl_List.headval = Node("Monday")

#Node for each day of the week
tues = Node("Tuesday")
wed = Node("Wednesday")
thur = Node("Thursday")
fri = Node("Friday")
sat = Node("Saturday")
sun = Node("Sunday")

#Lets link this list (Yay :D)
sl_List.headval.nextval = tues
tues.nextval = wed
wed.nextval = thur
thur.nextval = fri
fri.nextval = sat
sat.nextval = sun

sl_List.insertMiddle(wed,"Middle day")
sl_List.insertEnd("End day")
sl_List.insertBeginning("Beginning day")
sl_List.printList()
print("\nCool right next lets utilize our removal method to fix list\n")
sl_List.remove("Middle day")
sl_List.remove("End day")
sl_List.remove("Beginning day")
sl_List.printList()