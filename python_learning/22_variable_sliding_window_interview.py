
# Longest Substring with At Most K Distinct Characters
# s = "aaabbccd"
# k = 2
# output : 5

s = "aaabbccd"
k = 2
l=0
r=0
dic = {}
max_length = 0
size = 0
crt_len = 0

for r in range(len(s)):
    if s[r] in dic:
        dic[s[r]]+=1
    if s[r] not in dic:
        dic[s[r]]=1
    size= len(dic)
    while(size>k):
        if s[l] in dic:
            dic[s[l]]-=1
        if dic[s[l]]==0:
            del(dic[s[l]])
        l+=1
        size=len(dic)
    crt_len = r - l + 1
    if crt_len > max_length:
        max_length = crt_len
    
print(max_length)               # complexity : O(n) , space : O(n)

# Maximum Number of Vowels in a Substring of Size K
# a, e, i, o, u
# s = "abciiidef"
# k = 3
# output : 3

s = "abciiidef"
k = 3
count=0
max_count=0
for i in s[:3]:
    if i in "aeiou":
        count+=1
max_count=count
for i in range(1,len(s)-k+1):
    if s[i-1] in "aeiou":
        count-=1
    if s[i+k-1] in "aeiou":
        count+=1
    max_count=max(count,max_count)
print(max_count)                # complexity : O(n) , space : O(1)


# Maximum Sum Subarray of Size K
# arr = [2, 1, 5, 1, 3, 2]
# k = 3
# output : 9

arr = [2,1,5,1,3,2]
k = 3
sum = 0
max_value = 0
for i in range(k):
    sum+=arr[i]
max_value = sum

for i in range(1,len(arr)-k+1):
    sum = sum - arr[i-1]
    sum = sum + arr[i+k-1]
    max_value = max(sum,max_value)
print(max_value)                # complexity : O(n), space complexity : O(1)


# Longest Subarray with Sum ≤ K 
# arr = [2, 1, 5, 2, 3, 2]
# k = 7
# output : 3
# arr = [1, 2, 10, 1, 1]
# k = 4
# output : 2

arr = [1, 2, 10, 1, 1]
k = 4
lenth=0
sum=0
l=0
r=0
max_len=0

for i in range(len(arr)):
    sum+=arr[i]
    while sum>k:
        sum-=arr[l]
        l+=1
    if sum<=k:
        lenth= i - l + 1
    
    max_len=max(lenth,max_len)
print(max_len)                    # complexity : O(n), space complexity : O(1)


# Minimum Size Subarray Sum
# arr = [2, 3, 1, 2, 4, 3]
# k = 7
# output : 2


arr = [2, 3, 1, 2, 4, 3]
k = 7
sum = 0
l=0
min_len = float('inf')
for r in range(len(arr)):
    sum+=arr[r]
    while (sum>=k):
        min_len=min(r-l+1,min_len)
        sum-=arr[l]
        l+=1
print(min_len)                     # complexity : O(n) , space complexity : O(n)

# Longest Subarray with At Most K Odd Numbers concept
# arr = [1, 1, 2, 1, 2, 3]
# k = 2
# output = 4
# refer notepad for concept


arr = [1, 1, 2, 1, 2, 3]
k = 2
l = 0
m_l = 0
count = 0
for r in range(len(arr)):
    if arr[r]%2!=0:
        count+=1
    while count>k:
        if arr[l]%2!=0:
            count-=1
        l+=1
    c_l= r - l + 1
    m_l = max(c_l,m_l)
print(m_l)                         # complexity : O(n) , space complexity : :O(n)


# Longest Subarray with At Most 2 Even Numbers
# arr = [1, 2, 3, 4, 5, 6, 1]
# k = 2
# output : 5

arr = [1, 2, 3, 4, 5, 6, 1]
k = 2
l = 0
count = 0
c_l=0
m_l=0
for r in range(len(arr)):
    if arr[r]%2==0:
        count+=1
    while count>k:
        if arr[l]%2==0:
            count-=1
        l+=1
    c_l= r-l+1
    m_l= max(c_l,m_l)
print(m_l)                        # complexity : O(n) , space complexity : O(1)    




        
        
        

