# Fixed size sliding window - k (constant).
# Variable size sliding window - window size depends on the condition . expand when valid . shrink when invalid.
# In variable sliding window - we use pointer concept - L = 0 , R = 0. we expand and shrink the pointer based on conditions.

# Basic simple example.
# Eg : When to stop the window expand.

s = "abcdef"
L=0
R=0

while(R<len(s)):
    print(s[L:R+1])
    R+=1                # complexity : O(n²). space complexity : O(n) - because it create new string

# Eg : remove duplicate character and prints the string
# s = "abca"
# output = "bca"

s = "abca"
l = 0
max_count = 0
for r in range(len(s)):
    while s[r] in s[l:r]:
        l+=1
    max_count = max (max_count,r - l + 1)
print(max_count)        # complexity : O(n²). space complexity : O(n)


# spend 3 hrs to understand the concept and complexity for this code.

# variable sliding window + set
# Eg : longest substring without repeating characters
# s = "abca"
# output = 3

s = "abba"
l = 0
r = 0
count = 0
max_count=0
seen = set()
for i in range(len(s)):
    while s[i] in seen:
        seen.remove(s[l])
        l+=1
        count-=1
        
    seen.add(s[i])
    count+=1
    max_count=max(max_count,count)

print(max_count)                    # complexity : O(n) , space complexity : O(n)

# another method for longest substring without repeating characters

s = "abca"
l = 0
seen = set()
count=0
m_l=0
for r in range(len(s)):
    while s[r] in seen:
        seen.remove(s[l])
        l+=1
    seen.add(s[r])
    m_l=max(r-l+1,m_l)
print(m_l)                         # complexity : O(n) , space complexity : O(n)


# Count Distinct Characters in Every Window of Size K
# s = "aabcbcdbca"
# k = 3
# output : [2, 3, 3, 2, 3, 3, 3, 3]

s = "aabcbcdbca"
k = 3
L = 0
R = 0

dic = {}
count = 0
max_count=[]
for i in range(k):
    if s[i] in dic:
        dic[s[i]]+=1
    else:
        dic[s[i]]=1
count = len(dic)
max_count.append(count)

for i in range(1,len(s)-k+1):
    if s[i-1] in dic:
        dic[s[i-1]]-=1
    if s[i+k-1] in dic:
        dic[s[i+k-1]]+=1
    if s[i+k-1] not in dic:
        dic[s[i+k-1]]=1
    if dic[s[i-1]] == 0:
        del(dic[s[i-1]])
    count = len(dic)
    max_count.append(count)
print(max_count)                # complexity : (n) , space complexity : O(k)



    