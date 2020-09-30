'''Implementation of  the following operations of a queue using stacks.
enqueue(x) -- Push element x to the back of queue.
dequeue() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
'''
class Queue:
    def __init__(self):
	    self.items = []
      
    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)


    def peek(self):
        return self.items[0]


    def is_empty(self):
        if self.items == []:
            return True
        return False

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)  
print(queue.peek())   # returns 1
print(queue.dequeue())    # returns 1
print(queue.is_empty()) # returns false
 	  