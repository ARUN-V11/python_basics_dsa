#int

a=12312343
type(a)

#float 

x=2.5e4
type(x)

#complex

c1=2+3j
c2=3+4j
sum = c1+c2
print(sum)

#converting - converting the data

z=24.56
type(z)

int(z)

#boolean true = 1 , false = 0

# sequence in python: group of elements or an item

# string: group of characher or letters

# list: can store different type of elements. the element shoul dbe enclosed by the square bracket
# eg[] - list are mutual in nature

a = [1,3,4]
type(a)

# tuple: can store the different type of element. tuple can not modify
t = (1,2,3,4,5,6)
type(t)

# byte: grp of byte numbers
# positive integer from 0 to 255. can't even store negative number.
# we cannot modify or edit any number in byte type array

e = [10,23]
ex=bytes(e)
type(ex)

# byte array: similar to byte datatype. can be modified.

e = [10,23,43,54]
type(e)
ex = bytearray(e)
type(ex)

ex[0]= 24
print(list(ex))

for i , v in enumerate(ex):
    print(i,v)

# Range : sequence of number. not modified

r = range(5)
print (r)

for i in range(0,5):
    print(i)

# set: unordered collection of elements.it mutualable. does not accept duplicate elements.
# it can be modify by using remove and update. symbol {}

s = {10,20,30,5,54,5}
print (s)

# frozenset: can't be modified.

l= [10,23,43,54]
f = frozenset(l)
type(f)
f.update([36])

# mapping type: group of elemets in the form of key value pairs.

s = {10:"kamal",11:"arun"}
s[10]='kamal'
s[11]='aapp'
print(s)

# literals: constant value that is stored into variables.

a = 10   # numeric literals
a = 'hi' # string
a = True # boolean
