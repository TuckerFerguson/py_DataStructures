"""
@author Tucker Ferguson

2/28/2020

@descript Implementation of a Queue, using python

"""


class queue:
#initialize an empty list for our queue
    def __init__(self):
        self.queue = []

#Enqueue new values
    def enqueue(self,val):
        self.queue.append(val)
        return True
#Dequeues items, checks for empty queue    
    def dequeue(self):
        if(len(self.queue) > 0):
            temp = self.queue[0]
            self.queue = self.queue[1:len(self.queue)]
            print(temp)
            return temp
        else:
            print("Nothing left to dequeue")
    
    def nextQueuedItem(self):
        print(self.queue[0])
        

myQueue = queue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
print("1) myQueue: {}".format(myQueue.queue))
print("\n2) Dequeing time!")

#note we index 1 more than the actual length of the queue to test method functionality
for x in range(len(myQueue.queue) + 1):
        myQueue.dequeue()
print("\n3) finished :)\n")