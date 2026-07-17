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
