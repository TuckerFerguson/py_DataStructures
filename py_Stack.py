"""
@author Tucker Ferguson

2/28/2020

@descript Implementation of a Stack, using python

"""


class stack:
#initialize an empty list for our stack
    def __init__(self):
        self.stack = []

#add new values to stack
    def add(self,val):
        self.stack.append(val)
        return True
#removes and prints the last element of stack
    def pop(self):
        if(len(self.stack) > 0):
            temp = self.stack[-1]
            self.stack = self.stack[:len(self.stack)-1]
            print(temp)
        else:
            print("Nothing left to pop")
    
    def peakTop(self):
        print(self.stack[-1])

#Instantiate an object myStack of type stack()
myStack = stack()

#populate our stack
myStack.add("Jon")
myStack.add("Todd")
myStack.add("Rick Roll'd")
myStack.add("Tracy")

print("1) myStack: {}".format(myStack.stack))
print("\n2) popping time!")

#Test our pop() functionality
for x in range(2) :
    myStack.pop()
print("\n3) default exit due to rick rollage :)")