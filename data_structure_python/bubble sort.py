"""
bubble sort
"""

import random
def bubble(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

list = [random.randint(0,10) for i in range(10)]
print(list)
print(bubble(list))