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


#python operators
"""
arithmetic operators
relational 
assignment 
logical
bitwise
membership 
identity

"""

# arithmetic operators: addition (+), subtraction (-), multiplication (*), floor division (//)
#  modulus (%), division (/), exponentiation (**)

# assignment operators: assign(=), add and assign (+=), subtract and assign (-=), divide and assign (/=), 
# multiply and assign (*=), modulus and assign (%=), exponent and assign (**=), floor division and assign (//=)

# unary operator: unary minus (-a). not operator (not a)

a = True  # not a false
a = False # not a true


# comparison operators: < - less than, <= - less than or equal to, != not equal to, == - equal to 
# >= - greater than or equal to, > - greater than.

# logical operators: not, AND, OR 

a = 20
b = 20
a<=b

if (a>b and a==b):
    print("True")
else:
    print("False")

if (a>b or a==b):
    print("True")
else: 
    print("False")


# boolean operator: and , or , not 

a = True
b = False

a and b
a or b

# bitwise operators in python: bitwise AND (&), bitwise OR (|), bitwise XOR (^), bitwise 1's complement (-)
# left - shift (<<), right -shift (>>), bitwise NOT (~)

# 1 2 4 8 16 32
# 0 0 1
# 1 0 1
# 0 0 1


a = 4 
b = 5
a&b


# order of evaluation : bodmas (), ** , *, /, %, //, +, -

# output statement: print(), \n - new line, \t - space

a = 10
b = 20
print(a,b, sep = ",") 
print(f"value of {a,b}")


# formatted string: %i, %d - integer, %s - string, %f - float, %c - one character.

a = 10
b = 20
print("a=%s b=%i" %(a,b))

age = 30
name = "Bob"
salary = 50000.50
print("Name: %s, Age: %d, Salary: $%.2f" % (name, age, salary))

# 1. number is zero or positive or negative

n =int( input("enter number: "))
if (n>0):
    print("positive")
elif (n<0):
    print("negative")
else: 
    print("zero")
    
# 2. given number is between 1 to 10

n = int(input("enter number: "))
if(n>=1 and n<=10):
    print(True)
    
# 3. even or odd

n = int(input ("enter a number: "))
if (n%2==0):
    print("even")
else :
    print("odd")

# 4. display grp of message when condition is true

if(True):
    print("hi")

# while loop: it is useful to execute a grp of statement repeatedly. depending on wheither the condition is true or false

# for loop: then for loop is useful to iterate over the elements of the statement.

# for loop:

n = int(input("enter number: "))
for i in range (n):
    print (i)
    
# While loop:

n = 1
while(n<=10):
    print(n)
    n+=1
print("out of loop")

# break: keyword break the loop

n=1
while(n<=10):
    print(n)
    n+=1
    if(n==5):
        break

print("out of the loop")

# continue: keyword used to skip the loop

n=1
while(n<10):
    
    n+=1
    if(n==5):
        continue
    print(n)
print("out of loop")

# print even number

for i in range (1,10):
    if(i%2==0):
        print(i)
    
# Sum of numbers

n=5
sum=0
for i in range (5):
    sum+=i
print(sum)

# table of 8

n = 8
for i in range(1,11):
    print("8 * %d = %d"%(i,i*n))

# reverse the number: 

n = 123
rev = 0
while (n>0):
    rem = n % 10
    rev = (rev * 10) + rem
    n = n//10
print(rev)  # complexity - o(log n )

# print only odd digits in the given number

n = 427521
while(n>0):
    rem = n % 10
    if (rem % 2 != 0):
        print(rem)
    n = n//10

# nested loop:
'''
*
**
***
****
*****
******
'''
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        #print(*) this line prints the start and move to next line. we don't need to print with * in next. print with * within the line
        print("*", end="") # prints * with no newline, keeping stars on the same line
    print()

for i in range(1,n+1):
    for j in range (1,i+1):
        print(i,end ="")
    print()

# number of digits:

n = 123
count=0
while (n>0):
    count+=1
    n=n//10
print(count)  # complexity - o(log n )


# create a string: either double "" or single '' is called string

a = "asfdasdf"
print(a)

# length of a string: to count th eno of the string

s= "welcome to python class"
len(s)

# indexing in string:  positive , negative index
# positive index: left to right -> 0 1 2 3 4 5 
# negative index: right to left -> -1 -2 -3 -4 -5 

s = "welcome to python class"
print(s[0])

print(s[2])

print(s[-1])

# slicing the string: part or piece of string

str = "core python"

# syntax: stringname[start:stop:stepsize]

str[0:4]
str[0:4:2]
str[-4:-1]
str[::2]
str[-6::]
str[:4:]
str[::-1]
str[:-4:-1]

# repeating a string: repeating the value in the variable

s='python'
print(s*2)
print(s + " " + s)
print((s +" ")*2)
print(' '.join([s,s]))
print(f"{s} {s}")

# concatenation of a string: attaching of an two string

s1= "python"
s2= "programming"
print(s1+" "+s2)


# checking membership: check if a string or character is a member of another string or not. using "in" and "not in" operator

str = "python programming"
s = "python"
if (s in str):
    print("yes")

# comparing string:

s="box"
s1="boy"
print(s==s1)
print(s<s1) # compare them by taking them in english dictionary order

# removing space from string: rstrip(),strip(),lstrip()

s="    python programming    "
print(s.lstrip())
print(s.rstrip())
print(s.strip())

s=input()
for i in range(len(s)):
    print(s[i])

# syntax mainstring, find (substring, beggining, end)
s = "python programming"
sub = "pro"
print(s.find(sub,0,len(s)))

# finding string - find() , index()
s = "python programming"
sub = "xyz"
print(s.find(sub))
print(s.index(sub))


#counting string in a string: no of characters in the giving string

s="python programming"
sub = "p"
print(s.count(sub))

# string are immutable - cant be change

s="python"
s[0]='c'


# replacable
s1= "one"
s2= "two"
s2=s1
print(s2)

# replacing a string with another 

s="python programming"
print(s.replace("python","c"))

# splitting and joining string - string_name.split(' '), ' '.join(stringname)

number = "one-two-three-four"
l = (number.split("-"))
print(l)

sl = ",".join(l)
print(sl)

# change case of a string - s.upper(), s.lower() , s.swapcase()

s="python Programming"
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())

# checking starting and ending of a string - (mainstring.startswith(substring))

m = "it is python programming class"
s = "this"

print(m.startswith("this"))
print(m.endswith("class"))

# String testing method - isalnum(), isalpha(), isdigit(), islower(), isupper(), istitle(), isspace()

s = "abc123"
print(s.isalnum())

s="asdf"
print(s.isalpha())

s="3423"
print(s.isdigit())

s="ARUN"
print(s.isupper())

s="arun"
print(s.islower())

s="Python"
print(s.istitle())

s=" "
print(s.isspace())


# string reverse:
s= "python"
print(s[::-1]) #complexity o(n)

#Palindrome Check:
s="madam"
palindrome = s[::-1]
if (s==palindrome):
    print(True)
else:
    print(False) #complexity o(n)

#count vowel:
s= "education"
count = 0
for ch in range(len(s)):
   
    if (s[ch] == 'a' or s[ch] == 'e' or s[ch] == 'i' or s[ch]=='o' or s[ch]=='u'):
        count+=1
print(count) # complexity o(n)

#count characters:
s= "python programming"
print(s.count("p")) # complexity O(n)

# length of the string without inbuild function

s="python"
count = 0

for ch in s:
    count+=1
print(count) # complexity O(n)

# count number of word in string

s = "python programming"
count=1
for i in range(len(s)):
    if (s[i].isspace()):
        count+=1
print(count)  #complexity O(N)

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

#tuple
# creating tuple

t = (1,2,3,4,5)
l=(5,) # single element that element should followed by ,
print(l)

# accessing element

t = (1,2,3,4,5,6,7,8)
print(t[-1])

print(t[0:4])

# sum of the list

a = [1,2,3,4,5]
sum =0
for i in range(len(a)):
    sum+=a[i]
print(sum)

# write a program program to print the number of a specified list after removing even number from it .go to the editor

l=[1,2,3,4,5,6,7,8,9]
l2=[]
for i in range(len(l)):
    if(l[i]%2==0):
        l2.append(l[i])
print(l2)


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
for ch in s:
    if ch in repeated:
        repeated[ch]+=1
    else:
        repeated[ch]=1
print(repeated) # complexity: o(n)

# functions: 

def sum(a,b):
    print(a+b)
sum(10,20)     # complexity : O(1)

# even or odd 

def even_odd(num):
    if(num%2==0):
        print("even")
    else:
        print("odd") #complexity : o(1)  one modulo operation, one comparsion, one print
    
even_odd(10)
even_odd(1)

# returning result from functions

def sum(a,b):
    c=a+b
    return c  # complexity : O(1)

z=sum(10,20)
print(z)

# calling a functions:
"""
def my_funcation()
    print()
my_funcation()
"""
# arguments: information can be passed into funcations as arguments
# positional arguents: (exact position)

def simple(p,t,r):
    return (p*t*r)/100
p=2.4
r=3.5
t=4.0
simple(p,r,t) # complexity O(1)

#default arguments

def greed(name="arun"):
    print(name)
greed()
greed("raj")

#variable length arguments(*args)

def total(*args):
    s = 0
    for i in args:
        s+=i
    print(s)
total(10,20,30)

# global and local variable:

x=10
def display():
    x=20
    print(x)

display()
print(x)

# recursive function: a funcation calling itself (no.of times)
# eg : factorial

def fact(n):
    if (n==1):
        return 1
    else:
        return(n*fact(n-1))

fact(5)

def countdown(n):
    if n==0:
        return
    print(n)
    countdown(n-1)

countdown(5)


# array: arrays as same as list
#Problem 1: Sum of Array
arr= [1, 2, 3, 4, 5]
sum=0
for i in arr:
    sum+=i
print(sum) # complexity O(n)

# problem 2: max , min , reverse

arr=[10, 30, 15, 50, 20]
print(max(arr)) # complexity O(n) 
print(min(arr)) # complexity O(n)
arr.sort()
print(arr) # complexity O(n log n)
arr.reverse()
print(arr) # complexity O(n)

# problem 3:  count even numbers

arr= [1, 2, 3, 4, 5, 6]
count=0
for i in arr:
    if (i%2==0):
        count+=1

print(count)    # complexity o(n)

# problem 4: contains duplicate:

arr=[1,2,3,1]
duplicate=set()
for i in arr:
    if i in duplicate:
        print(True)
    else:
        duplicate.add(i) # complexity o(n)

# problem 5: remove duplicaite:

arr=[1,2,2,3,3,4]
without_duplicate=set()
for i in arr:
    if i not in without_duplicate:
        without_duplicate.add(i)  # complexity O(n)
        
    
print(without_duplicate)


    