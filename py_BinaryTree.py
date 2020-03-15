#
# @author Tucker Ferguson
# Date: 3/14/2020
# 
# @descript Creates Binary Tree Utilizing node class
# 
import random
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    def insert(self,data):
        if(self.data):
            if(data < self.data):
                if(self.left is None):
                    self.left = node(data)
                else:
                    self.left.insert(data)
            if(data > self.data):
                if(self.right is None):
                    self.right = node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def printTree(self):
        if(self.left):
            self.left.printTree()
        print(self.data)
        if(self.right):
            self.right.printTree()
            
    
root = node(69)
print("Create and Print Binary Tree using 8 random values (1-100)")
dataList = []
for x in range(8):
    dataList.append(random.randint(1,100))

for data in dataList :
    root.insert(data)

root.printTree()
print("Note: printTree() outputs the Binary Tree left to right")