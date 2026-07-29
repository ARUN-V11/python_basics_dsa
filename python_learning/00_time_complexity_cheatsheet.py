'''
==========================
Time Complexity Cheat Sheet
==========================
'''

# O(1) - Constant Time
# Example Problem:
# Find the element at index 3.

arr = [10, 20, 30, 40]
print(arr[2])              # Accessing an index


# -----------------------------------------


# O(log n) - Logarithmic Time
# Example Problem:
# Find 45 in a sorted array using Binary Search.

# [10,20,30,40,45,50,60,70]


# -----------------------------------------


# O(n) - Linear Time
# Example Problems:
# 1. Find maximum element.
# 2. Find minimum element.
# 3. Sum of all elements.
# 4. Frequency Count.
# 5. Prefix Sum.

arr = [10, 20, 30, 40]

for i in arr:
    print(i)


# -----------------------------------------


# O(n log n)
# Example Problems:
# 1. Sort an array (Merge Sort)
# 2. Sort an array (Heap Sort)

# [40,10,30,20] -> [10,20,30,40]


# -----------------------------------------


# O(n²) - Quadratic Time
# Example Problems:
# 1. Bubble Sort
# 2. Print all pairs
# 3. Selection Sort

arr = [10,20,30]

for i in arr:
    for j in arr:
        print(i, j)