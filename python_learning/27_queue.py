# Queue
# FIFO - First in first out.

"""
Operation               Meaning
Enqueue                 Add element at rear                     queue.append(x)
Dequeue                 Remove first element                    queue.pop(0)
Front / Peek            View first element                      queue[0]
Rear                    View last element                       queue[-1]

Enqueue   → append(x) → O(1) amortized
Dequeue   → pop(0)    → O(n)
Peek      → queue[0]  → O(1)
Rear      → queue[-1] → O(1)
Is Empty  → not queue → O(1)

"""

# creating basic queue:

queue = []

queue.append(10)    # enqueue
queue.append(20)    # enqueue
queue.append(30)    # enqueue

print(queue)
print(queue[0])     # front / peek -> 10
print(queue[-1])    # Rear → 30
print(queue)


# empty queue:

queue = []
if not queue:
    print("queue is empty")
else: 
    print(queue[0])


# function method using enqueue

def enqueue(queue,value):
    queue.append(value)

queue=[]
enqueue(queue,10) # O(1)
enqueue(queue,20) # O(1)
enqueue(queue,30) # O(1)     # complexity : O(1) , space complexity : O(1)

print(queue)


# function method using list

def dequeue(queue):
    queue.pop(0)

dequeue(queue)
print(queue)                # complexity : O(n) because remaining elements shift left  ->  , space complexity : O(1) pop(0) → O(1) time,


# function method using peek

def peek(queue):
    if not queue:
        return None         # None means “currently no value”.
    return queue[0]

print(peek(queue))          # complexity : O(1) , space complexity : O(1)


# function method using rear

def rear(queue):
    if not queue:
        return None
    return queue[-1]

print(rear(queue))          # complexity : O(1) , space complexity : O(1)


# problem 

def enqueue(value):
    queue.append(value)

def dequeue(queue):
    if not queue:
        return None
    return queue.pop(0)

def peek(queue):
    if not queue:
        return None
    return queue[0]

def rear(queue):
    if not queue:
        return None
    return queue[-1]

def is_empty(queue):
    return not queue



queue = []
enqueue(10)
enqueue(20)
enqueue(30)
print(queue)
print(dequeue(queue))
print(peek(queue))
print(rear(queue))
print(is_empty(queue))


# queue using class :

class Queue:
    def __init__(self):
        self.queue=[]

    # Enqueue - add element at rear
    def enqueue(self,value):
        self.queue.append(value)

    # dequeue - remove first element
    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.pop(0)

    # peek / front - view first element
    def peek(self):
        if not self.queue:
            return None
        return self.queue[0]

    # rear - view last element
    def rear(self):
        if not self.queue:
            return None
        return self.queue[-1]

    # isEmpty
    def isempty(self):
        return not self.queue

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.queue)
print(q.dequeue())
print(q.peek())
print(q.rear())
print(q.isempty())


# Dequeue

from collections import deque

queue = deque()

queue.append(10)            # O(1)
queue.append(20)            # O(1)
queue.append(30)            # O(1)

queue.popleft()             # O(1)
print(queue)


# Two-stack Queue:

def enqueue(stack1,value):
    stack1.append(value)
    return stack1

def dequeue(stack1,stack2):
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())
        return stack2.pop()
    return stack2.pop()
            
stack1 = []
stack2 = []

enqueue(stack1,10)
enqueue(stack1,20)
enqueue(stack1,30)
print(dequeue(stack1, stack2))  # 10
print(dequeue(stack1, stack2))  # 20
print(dequeue(stack1, stack2))  # 30
enqueue(stack1,40)
print(dequeue(stack1,stack2))               # complexity : O(1)  amortized , space complexity : O(n)

# circular queue:

def enqueue(value):
    global front,rear
    if (rear+1)%capacity==front:
        print("queue is full")
        return
    if front == -1:
        front = 0
    rear = (rear+1)%capacity
    queue[rear]=value

def dequeue():
    global front , rear
    if front == -1:
        print("queue is empty")
        return
    value = queue[front]
    queue[front]=None
    if front == rear:
        front = -1
        rear =-1
    else:
        front = (front+1)%capacity
    return value

def peek():
    global front , rear
    if front == -1:
        print("queue is empty")
    else :
        return queue[front]

def is_empty():
    return front == -1

def display():
    if front == -1:
        print("queue is empty")
        return
    i = front 
    while True:
        print(queue[i])
        if rear == i:
            break
        i = (i+1)%capacity

capacity = 5
queue = [None]*capacity
front = -1
rear = -1
enqueue(10)
enqueue(20)
enqueue(30)
print(queue)
print(dequeue())
print(peek())
print(is_empty())
enqueue(40)
enqueue(50)
enqueue(60)
display()

"""
circular queue time and space complexity 

function            time complexity         space complexity

enqueue             O(1)                    O(1)
dequeue             O(1)                    O(1)
peek                O(1)                    O(1)
is_empty            O(1)                    O(1)
display             O(n)                    O(1)

So interview-la if they ask Circular Queue space complexity → O(n).
If they ask display() auxiliary space → O(1).

queue = [None] * capacity

"""


