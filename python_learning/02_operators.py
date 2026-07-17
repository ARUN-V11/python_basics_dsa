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
