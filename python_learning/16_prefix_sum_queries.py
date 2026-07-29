# arr = [3, 8, 2, 5, 6]
# find sum from index 2 to index 4



'''

interviewers will ask question like this:

arr = [3, 8, 2, 5, 6]
left = 2
right = 4

'''

# To solve this you have to create prefix sum array and find the ans

arr = [3,8,2,5,6]
left = 2
right = 4
sum=0
prefix_sum=[]
for i in arr:
    sum+=i
    prefix_sum.append(sum)

arr_left=prefix_sum[left-1]
arr_right=prefix_sum[right]
sub=arr_right-arr_left
print(sub)                       # complexity : O(n). space complexity : O(n)

# below condition is must if left value is 0. above condition will return false answer because. 0 - 1 = -1.
# it goes last array value.

if left == 0:
    answer = prefix_sum[right]
else:
    answer = prefix_sum[right] - prefix_sum[left-1]

print(answer)