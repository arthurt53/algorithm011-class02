# 第九周学习笔记  
## 一、高级动态规划
### 1、多种情况下动态规划的状态转移方程  
* 爬楼梯问题  
```
# 递归公式：f(n) = f(n-1) + f(n-2), f(1) = 1, f(0) = 0

def f(n):
    x , y = 1, 1
    for i in range(1, n):
        y, x = x + y, y
    return y
```
* 不同路径  
```
# 递归公式：f(x, y) = f(x-1, y) + f(x, y-1)  

def f(x, y):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    for i in range(1, y + 1):
        for j in range(1, x + 1):
            dp[i][j] = dp[i - 1][j] + dp[j][i - 1]
    return dp[y][x]
```
* 打家劫舍  
```
# 状态转移方程定义方案一：
dp[i]状态的定义： max $ of robbing A[0 -> i]

dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

# 状态转移方程定义方案二：
dp[i][0]状态定义：max $ of robbing A[0 -> i] 且没偷 nums[i]
dp[i][1]状态定义：max $ of robbing A[0 -> i] 且偷了 nums[i]

dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]);
dp[i][1] = dp[i - 1][0] + nums[i];
```
* 最小路径和  
```
# 状态转移方程
dp[i][j]状态的定义： minPath(A[1 -> i][1 -> j])

dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + A[i][j]
```
* 股票买卖问题  
```
# 状态转移方程定义：
dp[i][k][0]状态定义：第 i 天未持仓且之前交易了k次  
dp[i][k][1]状态定义：第 i 天持仓且之前交易了k次  

for 0 <= i < n:
    for 1 <= k < K:
        for s in {0, 1}:
            dp[i][k][s] = max (buy, sell, rest)

初始状态：
dp[-1][k][0] = dp[i][0][0] = 0
dp[-1][k][1] = dp[i][0][1] = -infinity

状态转移方程：
dp[i][k][0] = max( 选择 rest , 选择 sell )
            = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max( 选择 rest , 选择 buy )
            = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
```
### 2、常见问题的解法(高阶DP）  
* 最长上升子序列  
```
class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num: i = m + 1 
                else: j = m
            tails[i] = num
            if j == res: res += 1
        return res
```
* 最长有效括号  
```
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0 for _ in range(len(s))]
        if len(s) < 2:
            return 0

        if s[1] == ')' and s[0] == '(':
            dp[1] = 2
        
        if len(s) == 2:
            return dp[1]

        for i in range(2, len(s)):
            if s[i] == '(':   
                dp[i] = 0
                continue
            if s[i] == ')':    
                if s[i-1] == '(':      
                    dp[i] = dp[i-2] +2
                if s[i-1] == ')' and s[i-1-dp[i-1]] == '(' and i-1-dp[i-1]>=0:   
                    dp[i] = dp[i-1-dp[i-1]-1] + 2 + dp[i-1]
        print(dp)        
        return max(dp)
```
* 最大矩形  
```
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxarea = 0

        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0': continue

                # compute the maximum width and update dp with it
                width = dp[i][j] = dp[i][j-1] + 1 if j else 1

                # compute the maximum area rectangle with a lower right corner at [i, j]
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    maxarea = max(maxarea, width * (i-k+1))
        return maxarea
```
* 不同的子序列  
```
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1 = len(s)
        n2 = len(t)
        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
        for j in range(n1 + 1):
            dp[0][j] = 1
        for i in range(1, n2 + 1):
            for j in range(1, n1 + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        #print(dp)
        return dp[-1][-1]
```
* 赛车  
```
class Solution(object):
    def racecar(self, target):
        K = target.bit_length() + 1
        barrier = 1 << K
        pq = [(0, target)]
        dist = [float('inf')] * (2 * barrier + 1)
        dist[target] = 0

        while pq:
            steps, targ = heapq.heappop(pq)
            if dist[targ] > steps: continue

            for k in xrange(K+1):
                walk = (1 << k) - 1
                steps2, targ2 = steps + k + 1, walk - targ
                if walk == targ: steps2 -= 1 #No "R" command if already exact

                if abs(targ2) <= barrier and steps2 < dist[targ2]:
                    heapq.heappush(pq, (steps2, targ2))
                    dist[targ2] = steps2

        return dist[0]
```
## 二、字符串算法  
### 1、基础概念及操作  
* Python和Java中的字符串是不可变的，修改字符串实际上是新建了一个字符串；而C++中的字符串是可变的  
* 遍历字符串  
```
for ch in 'abbc':
    print(ch)
```
* 字符串比较
```
==：使用==来比较两个字符串内的value值是否相同
is：比较两个字符串的id值（地址）
```
### 2、字符串匹配算法  
* 暴力法  O(mn)  
```
def forceSearch( txt, pat):
    M = len(txt)
    N = len(pat)
    for i in range(M - N + 1):
        for j in range(N + 1):
            if txt[i + j] != pat[j]:
                break
        if j == N:
            return i
         # 更加聪明？
         # 1. 预先判断: hash(txt.substring(i, M)) == hash(pat)
         # 2. KMP
    return -1
```
* Rabin-Karp 算法： 通过哈希函数可以算出子串的哈希值，然后将它和目标字符串中的子串的哈希值进行比较。  
*1、假设子串的长度为 M (pat)，目标字符串的长度为 N (txt)*  
*2、计算子串的 hash 值 hash_pat*  
*3、计算目标字符串txt中每个长度为 M 的子串的 hash 值（共需要计算 N-M+1次）*  
*4、比较 hash 值：如果 hash 值不同，字符串必然不匹配; 如果 hash 值相同，还需要使用朴素算法再次判断*  
```
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        d = 256
        q = 9997
        n = len(haystack)
        m = len(needle)
        h = pow(d,m-1)%q
        p = 0
        t = 0
        if m > n:
            return -1
        for i in range(m): # preprocessing
            p = (d*p+ord(needle[i]))%q
            t = (d*t+ord(haystack[i]))%q
        for s in range(n-m+1): # note the +1
            if p == t: # check character by character
                match = True
                for i in range(m):
                    if needle[i] != haystack[s+i]:
                        match = False
                        break
                if match:
                    return s
            if s < n-m:
                t = (t-h*ord(haystack[s]))%q
                t = (t*d+ord(haystack[s+m]))%q
                t = (t+q)%q
        return -1
```
* KMP 算法：当子串与目标字符串不匹配时，其实已经知道了前面已经匹配成功那一部分的字符（包括子串与目标字符串），设法利用这个已知信息，不要把“搜索位置” 移回已经比较过的位置，继续把它向后移  
```
def KMP_algorithm(string, substring):
    '''
    KMP字符串匹配的主函数
    若存在字串返回字串在字符串中开始的位置下标，或者返回-1
    '''
    pnext = gen_pnext(substring)
    n = len(string)
    m = len(substring)
    i, j = 0, 0
    while (i<n) and (j<m):
        if (string[i]==substring[j]):
            i += 1
            j += 1
        elif (j!=0):
            j = pnext[j-1]
        else:
            i += 1
    if (j == m):
        return i-j
    else:
        return -1
            
    
def gen_pnext(substring):
    """
    构造临时数组pnext
    """
    index, m = 0, len(substring)
    pnext = [0]*m
    i = 1
    while i < m:
        if (substring[i] == substring[index]):
            pnext[i] = index + 1
            index += 1
            i += 1
        elif (index!=0):
            index = pnext[index-1]
        else:
            pnext[i] = 0
            i += 1
    return pnext
 
if __name__ == "__main__":
    string = 'abcxabcdabcdabcy'
    substring = 'abcdabcy'
    out = KMP_algorithm(string, substring)
    print(out)
```
### 3、常见问题的解法  
* 最长回文串  
```
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j+1]
        return ans
```
* 通配符匹配  
```
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] | dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                
        return dp[m][n]
```
