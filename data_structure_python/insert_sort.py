
'''
insert sort
'''


# 手里牌，从小到大排，
# 如果摸到牌比手里牌小，手里牌向右挪,该牌插入有序队列
# 
def insert_sort(list): # O(n^2)
    for i in range(1,len(list)): # 摸到牌，无序列的第一张牌  O(n)
        j = i-1  # 和手里牌最大的（j处）
        tmp = list[i]
        # 和手里牌最右边（j处）（最大的）比较，如果手里最大牌<摸到牌，摸到牌放在后面(j+1处）；
        # 如果手里最大牌(j处)>摸到牌i，j处牌向右挪一个，到j+1处。
        # 摸到牌i 和j-1 处牌做比较
        while list[j] > tmp and j >= 0: # O(n)
            list[j+1] =list[j]
            j -= 1
        list[j+1] = tmp
    return list

li =[3,2,4,5,6,2,6,1]
print(insert_sort(li))
         
