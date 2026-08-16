"""
Concept:

Sliding Window = Move one continuous window instead of checking every subarray.

Why use Sliding Window?

- Avoid recalculating the same values again and again.
- Optimize Time Complexity from O(n²) to O(n).

Used for:

- Maximum Sum Subarray
- Minimum Sum Subarray
- Longest Substring
- Smallest Window
- Fixed Size Window
- Variable Size Window

Pattern:
Two Pointers (Same Direction)

"""

# Maximum Sum Subarray of Size K

# arr = [2,1,5,1,3,2]
# k = 3
# output = 9

arr = [2,1,5,1,3,2]
k = 3
sum = 0
max_value = 0
for i in range(k):
    sum = sum + arr[i]
max_value=sum

for i in range(1,len(arr)-k+1):
    sum = sum - arr[i-1]
    sum = sum + arr[i+k-1]
    max_value = max(sum,max_value)


print(max_value)                          # complexity : O(k) + O(n) = O(k+n) = O(n), space complexity : O(1) 

"""
Fixed Size Sliding Window

1. Calculate the first window.
2. Store it as the current answer.
3. Slide the window:
   - Remove the left element.
   - Add the new right element.
4. Update the answer.
5. Repeat.

Number of Windows = len(arr) - k + 1
Last Starting Index = len(arr) - k
"""

# Minimum Sum Subarray of Size K
# arr = [2,1,5,1,3,2]
# k = 3

arr = [2,1,5,1,3,2]
k = 3
sum = 0
max_value = 0
for i in range(k):
    sum+=arr[i]
min_value=sum

for i in range(1,len(arr)-k+1):
    sum = sum - arr[i-1]
    sum = sum + arr[i+k-1]
    min_value = min(min_value,sum)
print(min_value)                        # complexity : O(n) , Space complexity : O(1)


# Average of Every Window of Size K
# arr = [1,3,2,6,-1,4,1,8,2]
# k = 5

arr = [1,3,2,6,-1,4,1,8,2]
k = 5
sum = 0
value = 0
avg = []
for i in range(k):
    sum += arr[i]
value = sum/k
avg.append(value)

for i in range(1,len(arr)-k+1):
    sum = sum - arr[i-1]
    sum = sum + arr[i+k-1]
    value = sum/k
    avg.append(value)
print(avg)                                 # complexity : O(n), space complexity : O(n)


# Maximum Number of Vowels in a Substring of Size K
# s = "abciiidef"
# k = 3
# output = 3

s = "abciiidef"
k = 3
count = 0
value = 0
for ch in s[:k]:
    if ch in "aeiou":
        count+=1
value= count
for i in range (1,len(s)-k+1):
    
    if s[i-1] in "aeiou":
        count-=1

    if s[i+k-1] in "aeiou":
        count+=1
    value = max(value,count)

print(value)                    # complexity : O(n), space complexity : O(1)



# 1st learn Deque and try this problem
# First Negative Number in Every Window of Size K
# arr = [12, -1, -7, 8, -15, 30, 16, 28]
# k = 3

from collections import deque
arr = [12, -1, -7, 8, -15, 30, 16, 28]
queue = deque()
k = 3
ans = []
for i in range(k):
    if arr[i]<0:
        queue.append(i)
if queue:
    ans.append(arr[queue[0]])
else: 
    ans.append(0)
    
for i in range(1,len(arr)-k+1):
    if queue and queue[0] < i:
        queue.popleft()
    new_index=i+k-1
    if arr[new_index]<0:
        queue.append(new_index)
    if queue:
        ans.append(arr[queue[0]])
    else:
        ans.append(0)
print(ans)                              # complexity : O(n), space complexiy : O(k)

# Count Negative Numbers in Every Window of Size K
# arr = [12, -1, -7, 8, -15, 30, 16, 28]
# k = 3
# output = [2, 2, 2, 1, 1, 0]

from collections import deque
arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
count = 0
ans = []
for i in range(k):
    if arr[i]<0:
        count+=1
ans.append(count)

for i in range(1,len(arr)-k+1):
    if arr[i-1]<0:
        count-=1
    if arr[i+k-1]<0:
        count+=1
    if count:
        ans.append(count)
    else:
        ans.append(0)
print(ans)                              # complexity : O(n), space complexity : O(n)









        
            
        

