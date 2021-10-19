"""
select sort

https://www.bilibili.com/video/BV1mp4y1D7UP?p=14

"""

def select_sort_simple(list):# O(n^2) 
    new_list=[]
    for i in range(len(list)): # O(n)
        min_val = min(list) # O(n), 
        new_list.append(min_val)
        list.remove(min_val) # O(n), as elements after deleted item need to be moved forward
    return new_list
# 因为新建了list, 空间复杂度增加一倍
# improved version

# I don't wish to get a new list-> as it adds space complexity 
# find min, move it to the first position of the list, replace the original first item with this min value 

# 一趟记录最小数，放到第一个位置
# 再一趟记录无序区最小数，放到第二个位置
# ...
# key point: 有序区，无序区，无序区最小数位置

def select_sort(list): # O(n^2) 
    for i in range(len(list)-1): #i是第几趟，-1 是因为 最后一个数就是最大的了，不用动。O(n)
        # 遍历无序区
        min_loc = i #假定无序区的第一个值最小
        for j in range(i+1, len(list)): # range[), 前包后不包, 无序区
            if list[j]<list[min_loc]:
                min_loc = j
        list[i], list[min_loc] = list[min_loc], list[i]
    return list


li =[3,2,4,5,6,2,6,1]
print(select_sort_simple(li))

li2 =[3,2,4,5,6,2,6,1]
print(select_sort(li2))


