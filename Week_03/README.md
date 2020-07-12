# 第三周学习笔记  
## 一、递归  
### （一）概述
* 通过函数体进行的循环  
#### 1、特性  
* 向下进入不同的递归层，最后向上回到原来的递归层  
* 通过参数来进行函数层之间不同的传递变量  
* 每一递归层内的操作都是一份拷贝，仅有函数内的参数可以实现递归层间的传递  
#### 2、范型递归代码模板  
```
def recursion(level,param1,param2,...):
  # recursion terminator 递归终止条件
  if level > MAX_LEVEL：
    process_result
    return
    
  # process logic in current level 处理当前层逻辑  
  process(level,data...)
  
  # drill down  下探到下一层
  self.recursion(level + 1 ,p1,...)
  
  # reverse the current level status if needed 清理当前层的全局变量
```
#### 3、思维要点  
* 不要人肉进行递归，从写递归状态树到直接看递归函数  
* 找到最近最简方法，将其拆解成可重复解决的问题（重复子问题）  
* 数学归纳法思维  

#### 4、常见问题及解法  
* 二叉树的最近公共祖先  
```
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # recursion terminator 递归终止条件
        if not root or root == p or root == q: return root
        # drill down  下探到下一层
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # process logic in current level 处理当前层逻辑  
        if not left: return right
        if not right: return left
        return root
```
* 从前序与中序遍历序列构造二叉树  
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:  # 递归终止条件
            return
        root = TreeNode(preorder[0])  # 先序为“根左右”，所以根据preorder可以确定root
        idx = inorder.index(preorder[0])  # 中序为“左根右”，根据root可以划分出左右子树
        # 下面递归对root的左右子树求解即可
        root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
        root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])
        return root
```

### （二）分治  
* 根据递归状态树，将一个问题分解成多个子问题（split/merge）  
* 分治代码模板：
```
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 递归终止条件
  if problem is None: 
	print_result 
	return 
  
  # prepare data 处理当前逻辑
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 
  
  # conquer subproblems 解决子问题
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …
  
  # process and generate the final result 子问题的结果组合
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # revert the current level states
```
### （三）回溯  
* 不断在递归的每一层尝试解决问题，最终得到答案  
* 常用场景：N皇后问题、数独问题  
* 最坏情况下会返回指数级的复杂度  
#### 常见问题及解法  
* 组合  
```
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(i, k, tmp):
            if k == 0:
                res.append(tmp)
                return 
            for j in range(i, n + 1):
                backtrack(j+1, k-1, tmp + [j])
        backtrack(1, k, [])
        return res
```
* 全排列  
```
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return 
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res
```
* 全排列II(序列可重复）
```
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        visited = set()
        def backtrack(nums, tmp):
            if len(nums) == len(tmp):
                res.append(tmp)
                return
            for i in range(len(nums)):
                if i in visited or (i > 0 and i - 1 not in visited and nums[i-1] == nums[i]):
                    continue
                visited.add(i)
                backtrack(nums, tmp + [nums[i]])
                visited.remove(i)
        backtrack(nums, [])
        return res
```
