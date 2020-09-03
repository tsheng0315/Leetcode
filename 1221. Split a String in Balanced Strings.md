### 1221. Split a String in Balanced Strings

Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

 
```
Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".

Example 4:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'
```

```
Constraints:
1 <= s.length <= 1000
s[i] = 'L' or 'R'
```


## Solution:
I should use a stack. It seems intuitive. 
You just store each value, and make comparisons for subsequent values while either pushing or popping and count the total.

However, using a simple numerical count as an abstraction for a stack is much simpler and easier to deal with than lists (not to mention faster).

### Algorithm

1. Initialize `chars` (this will be our "stack") and `count`.
2. Loop through string and for every 'R' we `+1` and for every 'L' we `-1`.
3. Check if `chars` is `0` (i.e., whether the stack is empty or not). If it's empty, we increment count by 1 since that means we found a balanced string.

### code
```python
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        chars=0
        count=0
        
        for character in s:
            if character=='R':
                chars+=1
            else:
                chars-=1
            
            if chars==0:
                count+=1
        return count
 ```


