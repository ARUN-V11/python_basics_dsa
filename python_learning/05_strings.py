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

# string sort:

s  = "python"
sort_s = ''.join(sorted(s))
print(sort_s)


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
