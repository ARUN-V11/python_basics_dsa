# Two Pointers:
# Instead of using one pointer, we use two pointers.
# eg: arr = [10,20,30,40,50] left=0 right=len(arr)-1
# movement : left += 1, right -= 1
# why we use this. it optimize the complexity of code : O(n²) to O(n)

# two pointer : reverse the array, string, pallindrome , remove duplicate, two sum, remove zero's

"""
# Two Pointer Pattern:

1. Opposite Direction
left --->       <--- right

Used for: while loop
- Reverse
- Palindrome
- Two Sum
- Container With Most Water


2. Same Direction
left --->
right --->

Used for: for loop
- Remove Duplicates
- Move Zeroes

"""

# reverse the array : 

arr = [10, 20, 30, 40, 50]

left = 0
right = len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print(arr)                  # complexity : O(n). space complexity : O(1)


# reverse the string: 

s = "april"
s_l = list(s)
left=0
right=len(s)-1
while left<right:
    s_l[left],s_l[right]=s_l[right],s_l[left]
    left+=1
    right-=1
rev_str=''.join(s_l)
print(rev_str)              # complexity : O(n). space complexity : O(n)


s = "april"
rev=""
n=len(s)-1
while (n>=0):
    rev=rev+s[n]
    n-=1
print(rev)                  # complexity : O(n). space complexity : O(n)

# pallidrome

s = "hello"
left = 0
right = len(s)-1
is_pallindrome = True
while left < right:
    if s[left]!=s[right]:
        is_pallindrome= False
        break

    left+=1
    right-=1
print(is_pallindrome)        # complexity : O(n). space complexity O(n)

"""
Need to MODIFY a string?
→ Convert to list
→ Space = O(n)

Need only to READ/COMPARE a string?
→ Use string directly
→ Space = O(1)

"""

# array sort  : one pointer is enough

arr=[10,20,30,40,50]

is_sort=True
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        is_sort=False
        break
print(is_sort)              # complexity : O(n). space complexity O(1)


# remove duplicate elements from the sorted array. using two pointers
arr = [1,1,2,2,3,4,4]
left = 0
right= 1
for right in range (1,len(arr)):
    if arr[left]!=arr[right]:
        left+=1
        arr[left]=arr[right]
        
print(arr[:left+1])         # complexity O(n). space complexity O(1)


# interview problem : two sum (sorted array)

# arr = [2, 7, 11, 15]
# target = 9

arr = [2,7,11,15]
target = 9
value= []
left=0
right=len(arr)-1
while left<right:
    if arr[left]+arr[right]==target:
        value.append(arr[left])
        value.append(arr[right])
        break
    elif arr[left]+arr[right]>target:
        right-=1
    else:
        left+=1
print(value)            # complexity O(n) . space complexity : O(1)

# move all the zeros to the end: inteview problem
# arr = [0, 1, 0, 3, 12]
# [1,3,12,0,0]

arr = [0,1,0,3,12]
left = 0
right = 1
target = 0
for right in range(1,len(arr)):
    if arr[left]!=target or arr[right]!=target:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
print(arr)              # complexity : O(n). space complexity : O(1)


# water container problem:
# input : arr = [1,8,6,2,5,4,8,3,7]
# output : 49

arr = [1,8,6,2,5,4,8,3,7]
left = 0
right = len(arr)-1
max_value = 0
while left < right:
    width = right - left
    height = min(arr[left],arr[right])
    area = width * height
    max_value = max(max_value,area)
    if arr[left]<arr[right]:
        left+=1
    else:
        right-=1
print(max_value)        # complexity : O(n). space complexity : O(1)

"""
Container With Most Water (Two Pointers)

Formula:
Area = Width × Height

Width  = right - left
Height = min(arr[left], arr[right])

Algorithm:
1. Start with the maximum possible width.
   left = 0
   right = len(arr) - 1

2. Calculate:
   - width
   - height
   - area

3. Update the maximum area.

4. Move ONLY the pointer with the smaller height.
   Reason:
   The smaller height is the bottleneck.
   Moving the taller height cannot increase the current height.
   Only moving the smaller height gives a chance to find a larger area.

5. Repeat until left >= right.
t
Time Complexity : O(n)
Space Complexity : O(1)
"""


    


