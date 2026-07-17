# set: create set

s={10,20,30,30,40,50,50,60} # doesn't return duplicate values
print(s)

s={}   #empty set is not set. it an dictionary 
s=set() # is to create an empty set
print(type(s))

# add elements: 
s={10,20,30,40,50}
s.add(35)
print(s)

# remove set
s={10,20,30,40,50}
s.remove(20) #not value it thorws error.
s.discard(20) # safer version

# Transverse
s={10,20,30,40,50}
for i in s:
    print(i) # complexity o(n)

#membership check:
s={20,30,50}
print(20 in s) # complexity O(1) 

# union, intesection, difference 
s1={1,2,3,4,5,9}
s2={6,7,8,9}
s3=s1.union(s2)
print(s3)
s4=s1.intersection(s2)
print(s4)
s5=s1.difference(s2)
print(s5)

# converting list to set
l = [1,2,3,4,4,5,2,3,6,7]
s =set(l)
print(s)

# DSA usecase: find duplicates

l = [1,2,3,4,4,5,2,3,6,7]
s = set()
for x in l:
    if x in s:
        print("duplicate",x)
    s.add(x) #complexity: O(n)
