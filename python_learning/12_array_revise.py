# Reverse Traversal:
# print the array element from last to first

arr = [10,20,30,40,50]
n=len(arr)
while(n>0):
    print(arr[n-1])
    n-=1            #complexity: O(n). space complexity: O(1)


# Reverse Array:
# reversing the original array by creating new array

arr = [1,2,3,4,5]
rev_arr=[]
n=len(arr)
while(n>0):
    rev_arr.append(arr[n-1])
    n-=1
print(rev_arr)       # complexity: O(n). space complexity: O(n)

# Reverse String:
# reversing the string from last to string by creating new empty string

s = "python"
rev_s=""
n=len(s)
while(n>0):
    rev_s=rev_s+s[n-1]
    n-=1
print(rev_s)        # complexity: O(n). space complexity: O(n)

# Palindrome:

s = "madam"
rev_s=""
n=len(s)
while(n>0):
    rev_s=rev_s+s[n-1]
    n-=1
if (rev_s==s):
    print(True)
else:
    print(False)        # complexity: O(n). space complexity: O(n)

