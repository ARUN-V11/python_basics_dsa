# frequency count: means counting how many times each elements appears in an array.

# arr = [10, 20, 10, 30, 20, 10]
# Output:

# {
#     10: 3,
#     20: 2,
#     30: 1
# }

# concept : dictionaries

arr = [10,20,10,30,20,10]
frequency_count = {}
for i in arr:
    if i in frequency_count:
        frequency_count[i]+=1
    else:
        frequency_count[i]=1
print(frequency_count)             # complexity O(n). space complexity: O(n)


# Count character frequency

# concept : dictionaries

# Output:
# {
# 'b':1,
# 'a':3,
# 'n':2
# }

s = "banana"
frq = {}
for ch in s:
    if ch in frq:
        frq[ch]+=1
    else:
        frq[ch]=1
print(frq)              # complexity O(n). space complexity O(n)

                        # -------------------- 


# duplicate elements (using set)
# concept : set

arr = [10, 20, 10, 30, 20, 10]
duplicate_without=set()
duplication=set()
for i in arr:
    if i not in duplicate_without:
        duplicate_without.add(i)
    else:
        duplication.add(i)
print(duplication)      # complexity O(n). space complexity : 2(n) = O(n)

# duplicate elements (using dict)
# concept : dictionaries

arr=[10,20,10,30,20,10]
duplicate={}
duplicate_value=[]
for i in arr:
    if i in duplicate:
        duplicate[i]+=1
    else:
        duplicate[i]=1
for k,i in duplicate.items():
    if i>1:
        duplicate_value.append(k)
        print(k,i)
print(duplicate_value)     # complexity O(n). space complexity : O(n)

                        # -------------------- 


# first non - repeating elements:
# arr = [10, 20, 10, 30, 20, 40]
# output : 30
# concept : dict , hashing 

arr = [10,20,10,30,20,40]
frequency_count = {}
for i in arr:
    if i in frequency_count:
        frequency_count[i]+=1
    else:
        frequency_count[i]=1

for k,v in frequency_count.items():
    if v==1:
        print(k)
        break               # complexity : 2n = O(n). space complexity : O(n)

for i in arr:
    if frequency_count[i] == 1:
        print(i)
        break               # two approaches this is for interview. because it gets the value based on hashing

# most frequent element:
# arr = [10,20,10,30,20,10,30,30]
# output = 10
# concept : dictionaries , hashing

arr = [10,20,10,30,20,10,30,30]
frequency_count = {}
for i in arr:
    if i in frequency_count:
        frequency_count[i]+=1
    else:
        frequency_count[i]=1

print(frequency_count)
max_frequency=0
for k,v in frequency_count.items():
    if v>max_frequency:
        max_frequency=v
print(max_frequency)

for i in arr:
    if (frequency_count[i]==max_frequency):
        print(i)
        break                           # complexity : n+ k (unique elements)+n = 3n = O(n). space complexity : o(n)

# count unique elements
# arr = [10,20,10,30,20,40]
# output = 2
# concept : dict, hashing

arr = [10,20,10,30,20,40]
frequency_count = {}
unique_element_count=0
for i in arr:
    if i in frequency_count:
        frequency_count[i]+=1
    else:
        frequency_count[i]=1

for i in arr:
    if frequency_count[i]==1:
        unique_element_count+=1
print(unique_element_count)             # complexity : O(n). space complexity : O(n)



'''
==========================
Key Takeaways
==========================

1. Dictionary is used for frequency counting.

2. Set is used to check uniqueness.

3. Dictionary gives information.

4. Array gives order.

5. Frequency = count of occurrence.

6. Time Complexity:
   Most problems = O(n)

'''



        
