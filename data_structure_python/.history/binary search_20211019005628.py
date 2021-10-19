"""Write binary search function.

function take two inputs:
a Python list to search through; 
the value you're searching for.

Assume the list only has distinct elements,
(no repeated values)

elements are in a strictly increasing order.

Return the index of value, or -1 if the value
doesn't exist in the list.

visualisation:
https://www.cs.usfca.edu/~galles/visualization/Search.html
"""
def linear_search(input_array, val):
    for inedx, v in enumerate(input_array):
        if v == val:
            return index
        else: 
            return -1

def binary_search(input_array, val):
    low = 0
    high = len(input_array) -1 
    while low <= high: # 候选区有值
        mid = (low + high) //2
        if input_array[mid] == val:
            return mid
        elif input_array[mid] < val: #待查找值val，在mid右侧
            low = mid +1
        else: #input_array[mid] > val #待查找值val，在mid左侧
            high = mid -1
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print( binary_search(test_list, test_val1))
print( binary_search(test_list, test_val2))