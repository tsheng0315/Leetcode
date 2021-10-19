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
    for index, v in enumerate(input_array):
        if v == val:
            return index
        else: 
            return -1
# bilibili
def binary_search(input_array, val):
    low, high = 0, len(input_array) -1
    
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

# jiuZhang

# For a given sorted array (ascending order) and a target number, 
# find the LAST index of this number in O(log n) time complexity.
# bug version
class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        if not nums:
            return -1
        
        start, end = 0, len(nums)-1

        while start < end:  # 这里有个corner case, 当nums=[1，1] target = 1，start 不会被改变，无限循环
            mid = (start + end)// 2

            if nums[mid] == target:
                # start = mid # 不可以写mid+1, 因为可能mid就是最后一个target了
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        return -1

# correct version:
class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        if not nums:
            return -1
            
        start, end = 0, len(nums) - 1
        # 用 start + 1 < end 而不是 start < end 的目的是为了避免死循环
        # 在 first position of target 的情况下不会出现死循环
        # 但是在 last position of target 的情况下会出现死循环
        # 样例：nums=[1，1] target = 1
        # 为了统一模板，我们就都采用 start + 1 < end，就保证不会出现死循环
        while start + 1 < end:
            # python 没有 overflow 的问题，直接 // 2 就可以了
            # java和C++ 最好写成 mid = start + (end - start) / 2
            # 防止在 start = 2^31 - 1, end = 2^31 - 1 的情况下出现加法 overflow
            mid = (start + end) // 2
            
            # > , =, < 的逻辑先分开写，然后在看看 = 的情况是否能合并到其他分支里
            if nums[mid] < target:
                # 写作 start = mid + 1 也是正确的
                # 只是可以偷懒不写，因为不写也没问题，不会影响时间复杂度
                # 不写的好处是，万一你不小心写成了 mid - 1 你就错了
                start = mid
            elif nums[mid] == target:
                end = mid
            else: 
                # 写作 end = mid - 1 也是正确的
                # 只是可以偷懒不写，因为不写也没问题，不会影响时间复杂度
                # 不写的好处是，万一你不小心写成了 mid + 1 你就错了
                end = mid
                
        # 因为上面的循环退出条件是 start + 1 < end
        # 因此这里循环结束的时候，start 和 end 的关系是相邻关系（1和2，3和4这种）
        # 因此需要再单独判断 start 和 end 这两个数谁是我们要的答案
        # 如果是找 first position of target 就先看 start，否则就先看 end
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        
        return -1
赞同
2





               
