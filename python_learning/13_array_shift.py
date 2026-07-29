# array left shift: remove one element from left side

arr=[10,20,30,40,50]
for i in range(1,len(arr)):
    print(arr[i])           # complexity: O(n)

# array right shift: remove one element form right side

arr=[10,20,30,40,50]
for i in range(len(arr)-1):
    print(arr[i])           # complexity: O(n)        

# Create a new array after removing first element.

arr=[10,20,30,40,50]
left_remove=[]
for i in range(1,len(arr)):
    left_remove.append(arr[i])
print(left_remove)          # complexity: O(n)

# Create a new array after removing last element.

arr=[10,20,30,40,50]
right_remove=[]
for i in range(len(arr)-1):
    right_remove.append(arr[i])
print(right_remove)         # complexity: O(n)
