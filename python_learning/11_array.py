# array transverse : to visit the array elements one by one
arr = [10,20,30,40,50]
for i in arr:
    print(i)

# one - pass: finding an answer with one loop
count = 0
arr = [10,20,30,40,50]
for i in arr:
    if i%2==0:
        count+=1
print(count)

# track variable: variable used to store an answer is called track variable
max_num = arr[0]

# linear search: checking the given target number from the begining of the array. until the target is found or the array ends.
arr = [10, 20, 30, 40, 50]
target = 30
found = False
for i in arr:
    if (i == target):
        found = True
        break

if (found == True):
    print("element found")
else:
    print("no element found")


# find maximum element in an array without max()

arr = [12, 45, 7, 89, 23]
arr1=arr[0]
for i in range (1,len(arr)):
    if (arr[i]>arr1):
        arr1=arr[i]
print(arr1)             # complexity : o(n). space complexity : o(1) because extra variable count fixed arr1=arr[0]

# find minimum element in an array without min()

arr = [12, 45, 7, 89, 23]
arr1= arr[0]
for i in range (1,len(arr)):
    if (arr[i]<arr1):
        arr1=arr[i]
print(arr1)             # complexity : 0(n). space complexity : o(1) bbecause extra variable count fixed arr1=arr[0]

# find second largest element in an array

arr = [12, 45, 72, 89, 23]
largest= arr[0]
second= arr[0]
for i in range(1,len(arr)):
    if (arr[i]>largest):
        second=largest
        largest=arr[i]
    elif (arr[i]>second):
        second=arr[i]
print("second largest: ",second) # complexity o(n) space complexity : o(1)

# running sum concept: arr = [1, 2, 3, 4] , output =[1,3,6,10]

arr = [1, 2, 3, 4]
sum=0
run_sum=[]
for i in arr:
    sum+=i
    run_sum.append(sum)
print(run_sum)          # complexity: O(n) , space complexity : o(n)

# count odd number: arr = [12, 45, 7, 89, 23]

arr = [12, 45, 7, 89, 23]
count = 0
for i in arr:
    if i%2!=0:
        count+=1
print(count)            # complexity: O(n)

# sum of even numbers: arr = [12, 45, 7, 89, 23]

arr = [12, 45, 7, 89, 23]
sum=0
for i in arr:
    if i%2==0:
        sum+=i
print(sum)              # complexity : O(n)

# linear search : return index
# arr = [12, 45, 7, 89, 23]
# target = 89
# output = 3

arr = [12, 45, 7, 89, 23]
target = 89
count = 0
for i in arr:
    if(i!=target):
        count+=1
    else: 
        break
print(count)            # complexity : O(n) . space complexity: O(1)


