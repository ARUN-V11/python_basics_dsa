# Container With Most Water
# arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]

arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
l = 0
r = len(arr)-1
width = 0
height = 0
max_value=0
while (l<r):
    width = r - l
    height = min(arr[l],arr[r])
    area = width*height
    max_value = max (max_value,area)
    if arr[l]<arr[r]:
        l+=1
    else:
        r-=1
print(max_value)                # complexity : O(n), space complexity : O(1)


# two sum 
# arr = [2,7,11,15]
# target = 9
# output : 0 1

arr = [2, 7, 11, 15]
target = 9
l = 0
r = len(arr)-1
c_l=0
while l<r:
    c_l=arr[l]+arr[r]
    if c_l>target:
        r-=1
    elif c_l<target:
        l+=1
    else:
        break
print(l,r)                      # complexity : O(n) , space complexity : O(1)


# 3 sum problem
# arr = [-1, 0, 1, 2, -1, -4]
# target = 0
# output : 
# 1 2 5
# 1 3 4
# 2 3 4

arr = [-1, 0, 1, 2, -1, -4]
target_value = 0
arr.sort()
left = 0
c_sum = 0

for i in range(len(arr)):
    target = i
    left = i+1
    right = len(arr)-1
    while left<right:
        c_sum = arr[target]+arr[left]+arr[right]
        if c_sum<target_value:
            left+=1
        elif c_sum>target_value:
            right-=1
        else:
            print(target,left,right)
            left+=1
            right-=1

"""
Sorting       → O(n log n)
3Sum search   → O(n²)

Total         → O(n log n + n²)
              → O(n²) ✅

Space 

"""

# same 3 sums problem print unique elements
# output : 
# 1 2 5
# 1 3 4


arr = [-1, 0, 1, 2, -1, -4]
target_value = 0
current_sum = 0
arr.sort()
for i in range(len(arr)-2):
    target = i
    left = i+1
    right = len(arr)-1
    if i>0 and arr[i]==arr[i-1]:
        continue
    while left<right:
        current_sum= arr[target]+arr[left]+arr[right]
        if current_sum<target_value:
            left+=1
        elif current_sum>target_value:
            right-=1
        else:
            print(target,left,right)
            l_v = arr[left]
            r_v = arr[right]
            while left<right and arr[left]==l_v:
                left+=1
            while left<right and arr[right]==r_v:
                right-=1                            # complexity : O(n²) , space complexity : O(1)

        


