# Stack 
# LIFO - last in first out
"""
Stack       Python List

push        append()
pop         pop()
peek        stack[-1]

"""

# push - add
stack = []
stack.append(5)
stack.append(10)
stack.append(15)
print(stack)

# pop - remove
stack.pop()
stack.pop()
stack.pop()

# peek - stack[-1]
stack[-1]
print(stack)

# check stack is empty
stack = []
if not stack:
    print("stack is empty")         # complexity : O(1) , space complexity : O(1)


# reverse the string using stack: 
s = "hello"
stack = []
result = ""
for i in range(len(s)):
    stack.append(s[i])
while stack:
    result+=stack.pop()
print(result)                     # complexity : O(n) , space complexity : O(n)        


# peek/top
stack = [5, 10, 15, 20]
print(stack[-1])


# valid parenthesis
# s = "()[]{}"
# output = True

s = "((("
isValid=True
stack = []
mapping = {
    ')':'(',
    ']':'[',
    '}':'{'
}
for ch in s:
    if ch in "([{":
        stack.append(ch)
    else:
        if not stack or stack[-1]!=mapping[ch]:
            isValid=False
            break
        stack.pop()
if stack:
    isValid=False
print(isValid)                  # complexity: O(n), space complexity : O(n)



# Min Stack — Stack with O(1) getMin()
stack = []
min_stack = []
stack.append(5)
stack.append(3)
stack.append(7)
stack.append(2)
for i in range(len(stack)):
    current=stack[i]
    if not min_stack:
        min_stack.append(current)
    elif current<=min_stack[-1]:
        min_stack.append(current)
min_stack_value = min_stack[-1]
print(min_stack_value)          # complexity : O(n), space complexity : O(n)
        
# postfix expression
# question : 5 3 2 * + 4 -
# output : 7

s = ["5", "3", "2", "*", "+", "4", "-"]
stack = []
mapping = "+-*/"
for token in s:
    if token.isnumeric():
        stack.append(int(token))
    else:
        b = stack.pop()
        a = stack.pop()
        match token:
            case "+":
                result = a + b
                stack.append(result)
            case "-":
                result = a - b
                stack.append(result)
            case "*":
                result = a * b
                stack.append(result)
            case "/":
                result = int(a/b)
                stack.append(result)
print(stack)                            # complexity : O(n), space complexity : O(n)


# Monotonic stack:

# Maintain increasing order:
# arr = [5, 2, 6, 1, 4, 3, 7]
# output = [1, 3, 7]

arr = [5, 2, 6, 1, 4, 3, 7]
stack = []

for i in arr:
    current = i
    while stack and current < stack[-1]:
        stack.pop()
    stack.append(current)
print(stack)                            # complexity : O(n), space complexity : O(n)


# Maintain decreasing order:
# arr = [5, 8, 3, 7, 2, 6, 1]
# stack = []

arr = [5, 8, 3, 7, 2, 6, 1]
stack = []

for i in arr:
    current = i
    while stack and current > stack [-1]:
        stack.pop()
    stack.append(current)
print(stack)                            # complexity : O(n), space complexity : O(n)


# NEXT greater element:
# arr = [6, 3, 8, 4, 10, 2]
# output : [8, 8, 10, 10, -1, -1]

arr = [6, 3, 8, 4, 10, 2]
stack = []
result = [-1]*len(arr)
for i in range(len(arr)):
    current = arr[i]
    while stack and current > arr[stack[-1]]:
        result[stack[-1]]=current
        stack.pop()
    stack.append(i)
print(result)                            # complexity : O(n) , complexity : O(n)


# NEXT smaller element:
# arr = [6, 3, 8, 4, 10, 2]
# output : [3, 2, 4, 2, 2, -1]

arr = [6, 3, 8, 4, 10, 2]
stack = []
result = [-1]*len(arr)
for i in range(len(arr)):
    current = arr[i]
    while stack and current<arr[stack[-1]]:
        result[stack[-1]] = current
        stack.pop()
    stack.append(i)

print(result)                           # complexity : O(n) , complexity : O(n)


# stock span
# prices = [100, 80, 60, 70, 60, 75, 85]
# [1, 1, 1, 2, 1, 4, 6]

prices = [100, 80, 60, 70, 60, 75, 85]
stack = []
result = [1]*len(prices)
for i in range(len(prices)):
    current = prices[i]
    count = 1
    while stack and current >= prices[stack[-1]]:
        stack.pop()  
    if not stack:
        result[i] = i + 1
    else:
        result[i] = i - stack[-1]
    stack.append(i)
print(result)                           # complexity : O(n) , space complexity : O(n)



# Daily temperatures
# temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# output : [1, 1, 4, 2, 1, 1, 0, 0]

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
stack = []
result = [0]*len(temperatures)
for i in range(len(temperatures)):
    current= temperatures[i]
    while stack and temperatures[stack[-1]]<=current:
        result[stack[-1]]= i - stack[-1]
        stack.pop()
    stack.append(i)
print(result)                           # complexity : O(n) , space complexity : O(n)