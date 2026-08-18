# Two Pointers
# Used to track two positions in an array/string.
# L - left pointer
# R - right pointer
# arr = [1, 2, 3, 4, 5]
# L = 0
# R = len(arr) - 1
# Pointers move based on the problem condition.


# problem 1: Two Sum in a Sorted Array
# arr = [1,2,3,4,5,6]
# target = 6
# output : 2,4

arr = [1, 2, 3, 4, 6]
target = 6
l=0
r=len(arr)-1
current_sum=0
while l<r:
    current_sum=arr[l]+arr[r]
    if current_sum > target:
        r-=1
    elif current_sum < target:
        l+=1
    else:
        break
print(arr[l],arr[r])            # complexity : O(n) , space complexity : O(1)


# Problem 2 — Two Sum, but return indices
# arr = [2, 3, 4, 8, 11, 15]
# target = 12
# output : 2,3

arr = [2, 3, 4, 8, 11, 15]
target = 12
current_sum = 0
l = 0
r = len(arr)-1
while (l<r):
    current_sum=arr[l]+arr[r]
    if current_sum>target:
        r-=1
    elif current_sum<target:
        l+=1
    else: 
        break
print(l,r)                      # complextiy : O(n) , space complexity : O(1)


# Problem 3 — Count Pairs With Target Sum
# arr = [1, 2, 3, 4, 5, 6, 7]
# target = 8
# output : 3

arr = [1, 2, 3, 4, 5, 6, 7]
target = 8
current_sum = 0
l = 0
r = len(arr)-1
count=0

while (l<r):
    current_sum=arr[l]+arr[r]
    if current_sum>target:
        r-=1
    elif current_sum<target:
        l+=1
    else:
        count+=1
        l+=1
        r-=1
        
print(count)            # complexity : O(n), space complexity : O(1)


# Problem 4 — Count Unique Pairs With Target Sum
# arr = [1, 1, 2, 3, 3, 4, 5, 5, 6]
# target = 6

arr = [1, 1, 2, 3, 3, 4, 5, 5, 6]
target = 6
c_s = 0
count = 0
l = 0
r = len(arr)-1
while l<r:
    c_s = arr[l]+arr[r]
    if c_s>target:
        r-=1
    elif c_s<target:
        l+=1
    elif c_s==target:
        count +=1
        left_value = arr[l]
        right_value = arr[r]
        while l<r and arr[l]==left_value:
            l+=1
        while l<r and arr[r]==right_value:
            r-=1
        

print(count)            # complexity : O(n) , space complexity : O(1)

# Problem — Find Unique Pairs With Target Sum
# arr = [1, 2, 3, 4, 5, 6, 8, 9]
# target = 10
# output : 1 9, 2 8, 4 6

arr = [1, 2, 3, 4, 5, 6, 8, 9]
target = 10
l = 0
r = len(arr)-1
while l<r:
    c_s = arr[l]+arr[r]
    if c_s>target:
        r-=1
    elif c_s<target:
        l+=1
    elif c_s==target:
        left_value = arr[l]
        right_value = arr[r]
        print(arr[l],arr[r])
        while l<r and arr[l]==left_value:
            l+=1
        while l<r and arr[r]==right_value:
            r-=1                                # complexity : O(n) , space complexity : O(1)
        


        








