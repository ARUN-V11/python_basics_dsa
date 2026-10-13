# Hashmap 
# arr = [1, 2, 2, 3, 1, 2]
# output : {1: 2, 2: 3, 3: 1}
arr = [1, 2, 2, 3, 1, 2]
dic = {}
for i in range(len(arr)):
    if arr[i] in dic:
        dic[arr[i]]+=1
    else: 
        dic[arr[i]]=1
print(dic)                      # complexity: O(n), space complexity : O(1)

# two sum : unsorted array
# arr = [2, 11, 7, 15]
# output : 0 1

arr = [2, 11, 7, 15]
dic = {}
target_value = 9
current_sum = 0
for i in range(len(arr)):
    current = arr[i]
    needed = target_value - arr[i]
    if needed in dic:
        print(dic[needed],i)
    else:
        dic[arr[i]]=i           # complexity: O(n), space complexity : O(n)


# Non-Repeating Element
# arr = [4, 5, 1, 2, 1, 4, 5]
# output : 2

arr = [4, 5, 1, 2, 1, 4, 5]
dic = {}
for i in range (len(arr)):
    if arr[i] in dic:
        dic[arr[i]]+=1
    elif arr[i] not in dic:
        dic[arr[i]]=1
for k,v in dic.items():
    if v == 1:
        print(k)                # complexity : O(n) , space complexity : O(n)


# First Unique Element
# arr = [4, 5, 1, 2, 1, 4, 5, 8, 2, 9]
# output : 

arr = [4, 5, 1, 2, 1, 4, 5, 8, 2, 9]
dic = {}
for i in range (len(arr)):
    if arr[i] in dic:
        dic[arr[i]]+=1
    elif arr[i] not in dic:
        dic[arr[i]]=1
for k,v in dic.items():
    if v == 1:
        print(k)
        break                   # complexity : O(n) , space complexity : O(n)


# concept : seen / visited pattern

# Contains Duplicate : is array contains duplicate element print True

arr = [1, 2, 3, 4, 2]
seen = set()
isduplicate = False
for i in range(len(arr)):
    if arr[i] in seen:
        isduplicate=True
    else: 
        seen.add(arr[i])
print(isduplicate)              # complexity : O(n) , space complexity : O(n)

# First Repeated Element : print first duplicate elements

arr = [1, 2, 3, 3, 4, 2]
seen = set()

for i in range(len(arr)):
    if arr[i] in seen:
        print(arr[i])
        break
    else: 
        seen.add(arr[i])        # complexity : O(n) , space complexity : O(n)


# concept : grouping / mapping

# valid anagrams
# s = "listen"
# t = "silent"
# Output → True

s = "listen"
t = "silent"
isAnagaram = False
dic_s= {}
dic_t= {}

for i in range (len(s)):
    if s[i] in dic_s:
        dic_s[s[i]]+=1
    else:
        dic_s[s[i]]=1
for j in range (len(t)):
    if t[j] in dic_t:
        dic_t[t[j]]+=1
    else: 
        dic_t[t[j]]=1

if dic_s==dic_t:
    isAnagaram=True

print(isAnagaram)       # complexity : O(n) , space complexity : O(n)

# group anagrams

# arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
# output : {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}

arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
dic = {}
for word in arr:
    key=''.join(sorted(word))
    if key in dic:
        dic[key].append(word)
    else: 
        dic[key]=[word]
print(dic)                  # Complexity  : O(n * k log k) ,    Space Complexity : O(n * k)


# prefix sum + haspmap
# Longest Subarray With Sum K
# arr = [1, -1, 5, -2, 3]
# target = 3


arr = [1, -1, 5, -2, 3]
target = 3
sum = 0
max_l=0
dic={0:-1}
for i in range(len(arr)):
    sum+=arr[i]
    if sum not in dic:
        dic[sum]=i
    needed = sum - target
    if needed in dic:
        crt_index = i
        prv_index = dic[needed]
        sub_length=crt_index-prv_index
        max_l = max(max_l,sub_length)
print(max_l)                                # complexity : O(n) , space complexity : O(n)


# Subarray Sum Equals K
# arr = [1, 2, 3]
# target = 3
# output : 2 
# explanation : [1,2],[3] = 2



arr = [1,2,3]
target = 3
dic = {0:1}
count=0
prefix_sum=0
for i in range(len(arr)):
    prefix_sum+=arr[i]
    needed = prefix_sum-target
    if needed in dic:
        count+=dic[needed]
    if prefix_sum in dic:
        dic[prefix_sum]+=1
    if prefix_sum not in dic:
        dic[prefix_sum]=1
print(count)                        # complexity : O(n) , space complexity : O(n)













        



           
        
            
        
            
        
        
        
        
    
    


