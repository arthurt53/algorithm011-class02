# 第二周学习笔记  
## 一、高级一维数据结构  
### 1、哈希表（Hash table）  
* 工程实践：用户信息表、缓存（LRU Cache）、键值对存储（Redis）  
* 实现原理：将值通过哈希函数映射到对应位置，若对应位置存在多个值（哈希碰撞），可采取增加链表的方式进行存储（升维）  
* Python中的应用：set（可变集合）/froezen set（不可变集合）、dict（字典）  
* 查询：O(1)、若发生大量哈希碰撞则可能退化到O(n)  
* 增加：O(1)  
* 查询：O(1)  
#### 哈希表应用1：映射（Map）  
*key-value对，key值不重复*  
* Python中的map函数：  
```
map(func, *iterables)  #func --函数 *iterables--一个或多个序列
#一般会配合lambda函数一起使用
list(map(lambda x : x / 2 ,(1,2,3,4,5)))  # 输出为[0.5, 1.0, 1.5, 2.0, 2.5]
#map的替代：列表解析
[f(x) for x in iterable]
```
* dict（字典）
```
dict = {key1 : value1, key2 : value2 }     #新建
dict[key1]                                 #查询
dict.get(key, default=None)                #查询
dict[key1] = value3                        #修改
dict.pop(key[,default])                    #删除
del dict[key]                              #删除
```
#### 哈希表应用2：集合（Set）  
*不重复元素的集合*  
* 新建  
`set_test = set([iterable]) #此处的可迭代对象可以是字符串、列表、
* 增加  
`set_test.add()`
* 删除  
```
set_test.clear()        #清空集合
set_test.pop()          #取出第一个元素
set_test.remove(X)      #删除X元素，若没有则返回KeyError
set_test.discard(X)     #删除X元素，若没有则不进行任何操作
```
* 运算  
```
set_test1 & set_test2   #交集
set_test1 | set_test2   #并集
set_test1 - set_test2   #差集
```
## 二、基础二维数据结构  
### 1、树（Tree）  
* 基本元素：父亲节点、子节点  
* 树的实现：
```
class TreeNode:
  def __init__(self,val):
    self.val = val
    self.left,self.right = None, None
```
* 树的遍历：  
（1）前序遍历（根、左、右）：  
```
# 递归
def preorderTraversal(self, root):
  res = []
  def helper(root):
    if not root: return 
    res.append(root.val)
    helper(root.left)
    helper(root.right)
  helper(root)
  return res

# 迭代
def preorderTraversal(self, root):
  res = []
  if not root:
    return res
  stack = [root]
  while stack:
    node = stack.pop()
    res.append(node.val)
    if node.right:
      stack.append(node.right)
    if node.left:
      stack.append(node.left)
    return res
```
（2）中序遍历（左、根、右）：  
```
# 递归
def inorderTraversal(self, root):
  res = []
  def helper(root):
    if not root: return 
    helper(root.left)
    res.append(root.val)
    helper(root.right)
  helper(root)
  return res

# 迭代
def inorderTraversal(self, root):
  res = []
  if not root:
    return res
  stack = []
  cur = root
  while stack or cur:
    while cur:
      stack.append(cur)
      cur = cur.left
    cur = stack.pop()
    res.append(cur.val)
    cur = cur.right
  return res
```
（3）后序遍历（左、右、根）：  
```
# 递归
def postorderTraversal(self, root):
  res = []
  def helper(root):
    if not root: return 
    helper(root.left)
    helper(root.right)
    res.append(root.val)
  helper(root)
  return res

# 迭代
def postorderTraversal(self, root):
  res = []
  if not root:
    return res
  stack = [root]
  while stack:
    node = stack.pop()
    if node.left:
      stack.append(node.left)
    if node.right:
      stack.append(node.right)
    res.append(node.val)
    return res[::-1]
```
* 常用树结构：二叉树、二叉搜索树  
* 二叉搜索树（空树、左子树上的所有元素均小于或等于其根节点且右子树上的所有元素均大于或等于其根节点）  
查询（O(log n)）：  
```
def query(self, root, val):
	if root == None:
		return False
	if root.val == val:
		return True
	elif val < root.val:
		return self.query(root.left, val)
	elif val > root.val:
		return self.query(root.right, val)
```
插入新节点（O(log n)）： 
```
def insert(self, root, val):
	if root == None:
		root = TreeNode(val)
	elif val < root.val:
		root.left = self.insert(root.left, val)
	elif val > root.val:
		root.right = self.insert(root.right, val)
	return root
```
查询最大/最小值：  
```
def findMin(self, root):
	'''查找二叉搜索树中最小值点'''
	if root.left:
		return self.findMin(root.left)
	else:
		return root

def findMax(self, root):
	'''查找二叉搜索树中最大值点'''
	if root.right:
		return self.findMax(root.right)
	else:
		return root
```
删除节点（O(log n)）：  
```
def delNode(self, root, val):
	if root == None:
		return 
	if val < root.val:
		root.left = self.delNode(root.left, val)
	elif val > root.val:
		root.right = self.delNode(root.right, val)
	# 当val == root.val时，分为三种情况：只有左子树或者只有右子树、有左右子树、即无左子树又无右子树
	else:
		if root.left and root.right:
			# 既有左子树又有右子树，则需找到右子树中最小值节点
			temp = self.findMin(root.right)
			root.val = temp.val
			# 再把右子树中最小值节点删除
			root.right = self.delNode(root.right, temp.val)
		elif root.right == None and root.left == None:
			# 左右子树都为空
			root = None
		elif root.right == None:
			# 只有左子树
			root = root.left
		elif root.left == None:
			# 只有右子树
			root = root.right
	return root
```
***
树的面试题解法一般都是递归，为什么？  
答：因为树结构最基本的元素是根节点，左节点和右节点，所有树结构都是通过这3个元素的重复所构成的；而递归是通过反复自我调用来实现的，两者特性完全一致，所以树的面试题解法一般都是递归。  
***
### 2、堆（Heap）  
* 特性：可以迅速找到一堆数中的最大值或最小值  
* 常见的堆：二叉堆、斐波那契堆  
* 二叉堆：通过完全二叉树来实现，同时满足根节点始终大于/小于子节点【采用一位数组】  
#### 索引：  
（1）索引为i的左子节点的索引为2i + 1  
（2）索引为i的右子节点的索引为2i + 2  
（3）索引为i的左子节点的索引为(i - 1) // 2
#### 操作：  
* findmax（O(1)）  
* deletemax（O(log n)）  
* insert（O(log n)-二叉堆或O(1)-斐波那契堆）  
* 实现代码：  
```
class MaxHeap:
    heap = []
 
    def insert(num):
        MaxHeap.heap.append(num)	# 将数加入最大堆的末位
        MaxHeap.shift_up()		# 向上更新元素
 
    def shift_up():
        current_id = len(MaxHeap.heap) - 1
        parent_id = (current_id - 1)//2
        while current_id > 0:
            if MaxHeap.heap[parent_id] >= MaxHeap.heap[current_id]:
                break
            else:
                MaxHeap.heap[parent_id], MaxHeap.heap[current_id] = MaxHeap.heap[current_id], MaxHeap.heap[parent_id]
                current_id = parent_id
                parent_id = (current_id -1)//2

    def delete(num):
        temp = MaxHeap.heap.pop()	# 取出堆的最后一个数
        ind = MaxHeap.heap.index(num)	# 删除num，但索引位置不变
        MaxHeap.heap[ind] = temp	# 将取出的最后一个数填入该索引位
        MaxHeap.shift_down(ind)		# 向下更新元素
 
    def shift_down(ind):
        current_id = ind
        child_id_left = current_id * 2 + 1
        child_id_right = current_id * 2 + 2
        while current_id < len(MaxHeap.heap) - 1:
            #如果当前节点为叶子节点，shift_down完成
            if current_id * 2 + 1 > len(MaxHeap.heap) - 1:
                break
            #如果当前节点只有左孩子没有右孩子
            if current_id * 2 + 1 == len(MaxHeap.heap) - 1:
                if MaxHeap.heap[current_id] > MaxHeap.heap[-1]:
                    break
                else:
                    MaxHeap.heap[current_id], MaxHeap.heap[-1] = MaxHeap.heap[-1], MaxHeap.heap[current_id]
                    break
            #如果当前节点既有左孩子又有右孩子
            if MaxHeap.heap[current_id] > max(MaxHeap.heap[child_id_left], MaxHeap.heap[child_id_right]):
                break
            else:
                if MaxHeap.heap[child_id_right] > MaxHeap.heap[child_id_left]:
                    MaxHeap.heap[child_id_right], MaxHeap.heap[current_id] = MaxHeap.heap[current_id], MaxHeap.heap[child_id_right]
                    current_id = child_id_right
                    child_id_left = current_id * 2 + 1
                    child_id_right = current_id * 2 + 2
                else:
                    MaxHeap.heap[child_id_left], MaxHeap.heap[current_id] = MaxHeap.heap[current_id], MaxHeap.heap[child_id_left]
                    current_id = child_id_left
                    child_id_left = current_id * 2 + 1
                    child_id_right = current_id * 2 + 2

```
### 3、图（Graph）  
* 与树的差异：看是否有环，有环的是图，没环的是数  
* 基本构成元素：点（度-连接多少边）、边（权重）  
* 表达形式：邻接矩阵、邻接表（链表实现）  
![image](https://github.com/arthurt53/Graph_hub/blob/master/Graph.png)
## 三、复杂度总结
|      | 访问  | 搜索  | 新增  | 删除  |  空间复杂度  |
|  :----:  |  :----:  |  :----:  |  :----:  |  :----:  |  :----:  |
| 数组  |   O(1)  |  O(n)  |  O(n)  |  O(n)  |  O(n)  |
| 链表  |   O(n)  |  O(n)  |  O(1)  |  O(1)  |  O(n)  |
| 跳表  |   O(log(n))  |  O(log(n))  |  O(log(n))  |  O(log(n))  |  O(nlog(n))  |
| 栈  |   O(n)  |  O(n)  |  O(1)  |  O(1)  |  O(n)  |
| 队列  |   O(n)  |  O(n)  |  O(1)  |  O(1)  |  O(n)  |
| 双端队列  |   O(n)  |  O(n)  |  O(1)  |  O(log(n))  |  O(n)  |
