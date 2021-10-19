
'''
heap_sort(list)
para: list
return: list
'''

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
    return list


def heap_sort(list):
    n = len(list)-1
    for i in range((n-1)//2, -1, -1):
        sort(list, i, n)
    for j in range(n,-1,-1):
        list[0],list[j] = list[j], list[0]
        sort(list,0,j-1)

list = [i for i in range(10)]
import random
random.shuffle(list)
print(list)
print(heap_sort(list))

