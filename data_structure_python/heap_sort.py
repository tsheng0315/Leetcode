'''
heap_sort
https://www.bilibili.com/video/BV1mp4y1D7UP?p=25
'''


def heapfy(list, low, high):
    i = low
    j = 2*i+1
    tmp =list[i]
    while j <= high:

        if j+1 <= high and list[j] < list[j+1]: # 判断有无右孩子; j->大孩子
            j = j+1
        else: 
            pass

        if tmp < list[j]: # 判断堆顶暂存元素 和 大孩子大小
            list[i] = list[j]
            i = j # 大孩子所在位置成当前父节点
            j = 2*i +1

        else:
            list[i] = tmp
            break
    else:
        list[i] = tmp

def heap_sort(list): # O(nlogn)


# for i in range(10//2, -1, -1):
#     print(i)