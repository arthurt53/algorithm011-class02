# 第六周学习笔记  
## 一、动态规划算法（Dynamic Programming）  
* 本质上就是分治 + 最优子结构（动态递推）*  
### 1、关键点  
* 动态规划和递归或者分治没有根本上的区别（关键看有无最优的子结构）  
* 共性：找到重复子问题  
* 差异性：最优子结构、中途可以淘汰次优解  
### 2、动态规划问题的解决思路  
* 以斐波那契数列为例 *
* 自顶向下的解决思路(人脑思维）：  
```
def fib(n):
    memo = [0 for i in range(n+1)]
    if n<= 1:
        return n

    if memo[n] == 0:
        memo[n] = fib(n-1) + fib(n-2)

    return memo[n]
```
* 自底向上的解决思路（机器思维）：
```
def fib(n):
    memo = [0,1]
    for i in range(2 , n+1):
        memo.append(memo[i-1] + memo[i-2])

    return memo[n]
```
### 3、动态规划问题的解决步骤  
（1） 最优子结构：opt[n] = best_of(opt[n-1],opt[n-2],...)  
（2） 储存中间状态：opt[i]  
（3） 递推公式（状态转移方程/DP方程）  
ex: Fib:opt[n] = opt[n-1] + opt[n-2]  

### 4、常见问题解法  
* 最小路径和  
```
class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0: continue
                elif i == 0:  grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:  grid[i][j] = grid[i - 1][j] + grid[i][j]
                else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]
```
* 解码方法  
```
class Solution:
    def numDecodings(self, s: str) -> int:
        pp, p = 1, int(s[0] != '0')
        for i in range(1, len(s)):
            pp, p = p, pp * (9 < int(s[i-1:i+1]) <= 26) + p * (int(s[i]) > 0)
        return p
```
* 最大正方形  
```
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        
        maxSquare = maxSide * maxSide
        return maxSquare
```
* 任务调度器  
```
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ct = Counter(tasks)
        nbucket = ct.most_common(1)[0][1]
        last_bucket_size = list(ct.values()).count(nbucket)
        res = (nbucket - 1) * (n + 1) + last_bucket_size
        return max(res, len(tasks))
```
* 回文子串  
```
class Solution:
    def countSubstrings(self, s: str) -> int:
        L = len(s)
        cnt = 0
        # 以某一个元素为中心的奇数长度的回文串的情况
        for center in range(L):
            left = right = center
            while left >= 0 and right < L and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
        # 以某对元素为中心的偶数长度的回文串的情况
        for left in range(L - 1):
            right = left + 1
            while left >= 0 and right < L and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1

        return cnt
```
