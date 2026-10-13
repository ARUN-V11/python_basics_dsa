# stack using queue:

def push(value):
    queue.append(value)
    
    size = len(queue)-1
    while size >0:
        value = queue.pop(0)
        queue.append(value)
        size -= 1                               # complexity : O(n), space complexity : O(1)

def pop():
    if not queue:
        print("queue is empty")
        return
    return queue.pop(0)                         # complexity : O(n), space complexity : O(1)
    
def top():
    if not queue:
        print("queue is empty")
        return
    return queue[0]                             # complexity : O(1), space complexity : O(1)

def is_empty():
    return not queue                            # complexity : O(1), space complexity : O(1)

queue =[]
push(10)
push(20)
push(30)
x = pop()
print(x)
y= top()
print(y)
print(is_empty())


# First non-repeating characters in a stream
# Stream : a a b c
# output : a -1 b b 

from collections import deque
stream = "aabc"
queue = deque()
result = ""
frequence = {}

for ch in stream:
    if ch in frequence:
        frequence[ch]+=1
    if ch not in frequence:
        frequence[ch]=1
    queue.append(ch)
    while queue and frequence[queue[0]]>1:
        queue.popleft()
    if not queue:
        result+="-1 "
    else:
        result+=queue[0]+" "

print (result)                                  # complexity : O(n), space complexity O(n)


# Generate Binary Numbers from 1 to N
# Input : N = 5
# Output: ["1", "10", "11", "100", "101"]

from collections import deque

n = 5
queue = deque()
queue.append("1")

result = []

for i in range(n):
    value = queue.popleft()
    result.append(value)
    queue.append(value + "0")
    queue.append(value + "1")

print(result)                                   # complexity : O(n), space complexity : O(n)


# Sliding window maxing using queue concept:
# input case 1: arr = [1, 3, -1, -3, 5]
# input case 2: arr = [1,2,3,4,5,6]
# k = 3

from collections import deque

arr = [1, 3, -1, -3, 5]
k = 3
queue = deque()
result = []
for i in range (len(arr)):

    while queue and queue[0] <= i - k:
        queue.popleft()
    
    while queue and arr[queue[0]]<arr[i]:
        queue.pop()
    queue.append(i)

    if i >= k-1:
        result.append(arr[queue[0]])

print (result)                                  # complexity : O(n), space complexity : O(n)