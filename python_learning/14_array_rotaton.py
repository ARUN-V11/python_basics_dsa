# left rotation: print the 1st elements in array last.

arr = [10, 20, 30, 40, 50]
left_rotate=arr[0]
for i in range(1,len(arr)):
    print(arr[i])
print(left_rotate)                  # complexity : O(n). space complexity : O(1)

# right rotation: print the last element in array first

arr = [10, 20, 30, 40, 50]
right_rotate=arr[len(arr)-1]
print(right_rotate)
for i in range(len(arr)-1):
    print(arr[i])                   # complexity : O(n). space complexity : O(1)

# left rotation : create new array
# arr = [10, 20, 30, 40, 50]
# [20, 30, 40, 50, 10]

arr = [10,20,30,40,50]
left_rotation=[]
for i in range(1,len(arr)):
    left_rotation.append(arr[i])
left_rotation.append(arr[0])
print(left_rotation)                # complexity : O(n). space complexity: O(n)

# right rotation : create new array
#  arr = [10,20,30,40,50]
# [50,10,20,30,40]

arr = [10,20,30,40,50]
right_rotation=[]
right_rotation.append(arr[len(arr)-1])
for i in range(len(arr)-1):
    right_rotation.append(arr[i])
print(right_rotation)               # complexity : O(n). space complexity: O(n)

# left rotation using string:
# arr = ['A', 'B', 'C', 'D', 'E']
# ['B', 'C', 'D', 'E', 'A']

arr = ['A', 'B', 'C', 'D', 'E']
left_str_rotate=[]
for i in range(1,len(arr)):
    left_str_rotate.append(arr[i])
left_str_rotate.append(arr[0])
print(left_str_rotate)              # complexity : O(n). space complexity: O(n)

arr = ['A', 'B', 'C', 'D', 'E']
right_str_rotate=[]
right_str_rotate.append(arr[len(arr)-1])
for i in range(len(arr)-1):
    right_str_rotate.append(arr[i])
print(right_str_rotate)             # complexity : O(n). space complexity: O(n)


