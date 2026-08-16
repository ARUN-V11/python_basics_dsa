# Queue : Queue follows FIFO
# FIFO : FIRST IN FIRST OUT
# Ex : Ticket counter


# Operations:
# Insert : Enqueue - add at - back
# Remove : Dequeue - remove from - front

#  Example : below mentioned example is not for queue. it's list.pop(index). This helps to understand how queue works.

queue = []
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)

queue.pop(0)
queue.pop(1)
queue.pop(2)
print(queue)

# Queue example.

from collections import deque

queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)

print(queue)

queue.popleft()
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)

"""
Why use deque instead of list?

list.pop(0):
- Removes the first element.
- All remaining elements shift one position to the left.
- Time Complexity = O(n)

deque.popleft():
- Removes only the first element.
- Remaining elements DO NOT shift.
- Only the front pointer moves to the next element.
- Time Complexity = O(1)

Conclusion:
For Queue operations, use deque because removing from the front is much faster than list.pop(0).

"""
