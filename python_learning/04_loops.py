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
