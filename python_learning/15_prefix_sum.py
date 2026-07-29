# prefix sum : run sum concept
# arr = [1, 2, 3, 4, 5]
# [1,3,6,10,15]

arr = [1,2,3,4,5]
prefix_sum = []
sum=0
for i in arr:
    sum+=i
    prefix_sum.append(sum)
print(prefix_sum)           # complexity : O(n). space complexity : O(n)

# arr = [5,10,15]
# [5,15,30]

arr = [5,10,15]
prefix_sum = []
sum = 0
for i in arr:
    sum+=i
    prefix_sum.append(sum)
print(prefix_sum)           # complexity : O(n). space complexity : O(n)

# arr = [4,5,6,7]
# [4,9,15,22]
# 22

arr = [4,5,6,7]
sum = 0
prefix_sum=[]
for i in arr:
    sum+=i
    prefix_sum.append(sum)
print(prefix_sum)
print(sum)           # complexity : O(n). space complexity : O(n)

# arr = [3,1,4,2]
# print each sum

arr = [3,1,4,2]
sum = 0
for i in arr:
    sum+=i
    print(f"current sum : {sum}")          # complexity : O(n). space complexity : O(1)



