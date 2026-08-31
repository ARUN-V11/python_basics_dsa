# Dictionaries: key value pair
# key followed by value (key can't be modify)

d=[1,2,3,4,5] # list value based on index
print(d[0])

d={"0":"one","1":"two"}
print(d["1"])

# Add:
d["3"]="there"
print(d)

#delete:
del(d["3"])
print(d)

#membership
print("3" in d)

# method - clear(), copy(), key(), values(), idems(),pop()

# clear()- remove all key value pair from dic
d={"0":"one","1":"two"}
print(d)
d.clear()
print(d)

#copy
d={"0":"one","1":"two"}
d1=d.copy()
print(d1)


print(d.keys())

print(d.values())

print(d.items())

print(d.pop("1")) # before removing an elements it prints the values of that key

print(d)

# using for loop with dictionaries

d={"0":"one","1":"two","2":"three"}
for k in d:
    print(k) # it prints key

for i in d:
    print(d[i]) # it prints values

for k,v in d.items():
    print(f"{k}:{v}")

# converting list into dic:

k=[1,2,3]
v=['red','blue','green']
z=zip(k,v)
d=dict(z)
print(d)

# use case dsa concept : frequency count
'''
This single concept is used in:
Frequency Count
Anagram
Two Sum
Top K Frequent Elements
Many interview questions
'''
s="programming"
repeated={}
repeated_2=repeated
for ch in s:
    if ch in repeated:
        repeated[ch]+=1
    else:
        repeated[ch]=1
print(repeated) # complexity: o(n)

# dictionary with list:
# arr=["aet","tea","ate"]
# output: {'aet': ['tea', 'ate']}

arr=["aet","tea","ate"]
dic={}
key = arr[0]
dic[key]=["tea"]
dic[key].append("ate")
print(dic)

