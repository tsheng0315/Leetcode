
'''
heap_sort(list)
para: list
return: list
'''
import time
start_time = time.time()
def sort(list, low, high):
    i = low
    j = 2*i+1
    tmp = list[i]
    while j <= high:
        if j+1 <= high and list[j] < list[j+1]:
            j = j+1
        if tmp < list[j]:
            list[i] = list[j]
            i = j
            j = 2*i +1
        else: 
            break
    list[i] = tmp
   


def heap_sort(list): # O(nlogn)
    n = len(list)-1
    for i in range((n-1)//2, -1, -1): # O(nlogn)
        sort(list, i, n)
    for j in range(n,-1,-1): # O(nlogn)
        list[0],list[j] = list[j], list[0]
        sort(list,0,j-1)
    return list
    

list = [i for i in range(10000)]
import random
random.shuffle(list)
print(list)
print(heap_sort(list))

end_time= time.time()
gap = end_time - start_time
print(gap)