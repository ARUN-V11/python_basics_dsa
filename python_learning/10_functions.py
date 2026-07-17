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


     