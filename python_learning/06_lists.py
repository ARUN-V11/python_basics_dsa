# list - Aliasing and cloning list:
# creating list
l = []
s = list()
 
s=[10,20,30,40]
s1=["ravi","arun"]
s3=[10,"ravi",20,30.5]
print(type(s3))
 
li=[10,20,30,40,50,60]
l1=li
print(li)
print(l1)

#cloning / copy:

x = [10,20,30,50]
y= x[:] # defined x is cloned as y
x[0]=100
print(x)
print(y)

# create list using range():
l = list(range(1,10,2))
print(l)

# concatenation

x = [10,20,30,30,40]
y = [40,50,60]
print(x+y)

# list methods()

l=[1,2,3,4,5,6]
print(len(l))
print(l.count(4))
print(l.index(4))


# insert: append(), insert(), extend()

l = [1,2,3,4]
l.append(19)
print(l)
l.insert(1,5)
print(l)
l1= [12,2,34,2,2,5]
l.extend(l1)
print(l)

# delete: pop(), remove(), clear()

l=[10,20,40,30]
l.pop()
print(l)
l.remove(20)
print(l)
l.clear()
print(l)

#sort: sort(), reverse(),

l=[20,4,34,24,234,54,67]
l.sort()
print(l)
l.reverse()
print(l)

# sortwith reverse method
l.sort(reverse=True)
print(l)

# finding biggest and smallest element in list min(), max()

l = [10,3,24,5,6,756,34,80]
print(max(l))
print(min(l))

# add - append , update, del , remove

l=[23,32,43,54,34,66,43]
l.append(40)
print(l)
l[2] = 6 #update
print(l)
del l[1]
print (l)
l.remove(54)
print(l)

# finding common elements in 2 lists

l1= [1,2,3,4,5,67]
l2= [5,6,7,8,9]

s1=set(l1)
s2=set(l2)

s3=s1.intersection(s2)
print(s3)
l3=list(s3)
print(l3)

#nested list: list contain more than 1 list
a=[1,2,3,4,5,6,7,8]
b=[a,8,9,0]
print(b)
