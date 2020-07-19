# 第四周学习笔记  
## 一、遍历搜索算法   
*在树（图/状态集）中寻找特定结点，每个结点**访问一次，且仅访问一次***  
### 1、深度优先算法（DFS）  
* 遍历顺序：根节点 → 某一子树走到底 → 下一个子树循环  
* 代码模板：  
```
#1  递归写法
visited = set() 

def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 

	visited.add(node) 

	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)
      
#2  非递归写法（模拟递归）
def DFS(self, tree): 

	if tree.root is None: 
		return [] 

	visited, stack = [], [tree.root]

	while stack: 
		node = stack.pop() 
		visited.add(node)

		process (node) 
		nodes = generate_related_nodes(node) 
		stack.push(nodes) 

	# other processing work 
	...
```
### 2、广度优先算法（BFS）  
* 遍历顺序：根节点 → 所有子节点 → 所有子节点的子节点...  
* 代码模板：  
```
def BFS(graph, start, end):
# 利用队列（数组）来实现
    queue = []
    queue.append([start])
    visited.add(start)
    
    while queue:
        node = queue.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)
        
     # other processing work
     ...
```
### 3、常见问题解法  
* 单词接龙  
```
from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queue for BFS
        queue = [(beginWord, 1)]
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.pop(0)
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0
```
* 岛屿数量  
```
# 深度优先
class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = 0
        nr, nc = len(grid), len(grid[0])
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    self.dfs(grid, r, c)

        return num_islands

# 广度优先
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = "0"
                    neighbors = collections.deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                                neighbors.append((x, y))
                                grid[x][y] = "0"

        return num_islands
```
## 二、贪心算法  
### 1、定义  
在每一步都采取在当前状态下最好或最优的选择，从而希望找到全局最优解的算法  
### 2、与动态规划的区别  
动态规划会回退，而贪心算法不会  
### 3、应用场景  
解决最优化问题、用作辅助算法或直接解决一些要求结果不特别精确的问题    
### 4、贪心算法使用原则  
问题能够分解成子问题来解决，子问题的最优解能够递推到最终问题的最优解  
### 5、常见问题解法  
* 柠檬水找零  
```
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        i=j=0
        for k in bills:
            if k==5:i+=1
            elif k==10:j+=1;i-=1
            else:
                if j==0:i-=3
                else:i-=1;j-=1
            if i<0 or j<0:return False
        return True
```
* 买卖股票的最佳时机
```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0: profit += tmp
        return profit
```
* 分发饼干  
```
def findContentChildren(self, g, s):
    g.sort() #孩子数组
    s.sort() #饼干数组
    child = 0 #孩子 i
    cookie = 0 #饼干 j
    while child < len(g) and cookie < len(s):
        if g[child] <= s[cookie]: #能够满足一个孩子的胃口
            child += 1 #孩子饱了
        cookie += 1 #饼干吃了
    return child #返回被满足的孩子数
```
* 模拟行走机器人  
```
class Solution(object):
    def robotSim(self, commands, obstacles):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obstacleSet = set(map(tuple, obstacles))
        ans = 0

        for cmd in commands:
            if cmd == -2:  #left
                di = (di - 1) % 4
            elif cmd == -1:  #right
                di = (di + 1) % 4
            else:
                for k in xrange(cmd):
                    if (x+dx[di], y+dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x*x + y*y)

        return ans
```
## 三、二分查找  
### 1、能够使用二分查找的三个前提条件  
* 目标函数的单调性（递增/递减）  
* 目标存在上下界  
* 目标能够通过索引进行访问  
### 2、二分查找的代码模板  
```
left, right = 0, len(array) - 1 
while left <= right: 
	  mid = (left + right) / 2 
	  if array[mid] == target: 
		    # find the target!! 
		    break or return result 
	  elif array[mid] < target: 
		    left = mid + 1 
	  else: 
		    right = mid - 1
```
### 3、常见问题解法  
* 寻找旋转排序数组中的最小值  
```
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1          # 左闭右闭区间，如果用右开区间则不方便判断右值
        while left < right:                     # 循环不变式，如果left == right，则循环结束
            mid = (left + right) >> 1           # 地板除，mid更靠近left
            if nums[mid] > nums[right]:         # 中值 > 右值，最小值在右半边，收缩左边界
                left = mid + 1                  # 因为中值 > 右值，中值肯定不是最小值，左边界可以跨过mid
            elif nums[mid] < nums[right]:       # 明确中值 < 右值，最小值在左半边，收缩右边界
                right = mid                     # 因为中值 < 右值，中值也可能是最小值，右边界只能取到mid处
        return nums[left]                       # 循环结束，left == right，最小值输出nums[left]或nums[right]均可
```
* 使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方  
```
class
```
