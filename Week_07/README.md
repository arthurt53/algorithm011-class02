# 第七周学习笔记  
## 一、字典树（Trie）  
### 1、字典树的数据结构  
* 将字符串拆成单个字符进行存储，每个单词是整个路径上字符的合集  
* 典型应用：统计和排序大量的字符串，故常用于搜索引擎系统中的文本词频统计  
* 优点：最大限度减少无谓的字符串比较，查询效率比哈希表高  
### 2、字典树的核心思想  
* 空间换时间：利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的  
### 3、字典树的基本性质  
* 结点本身不存完整单词    
* 从根结点到某一结点，路径上经过的字符连接起来，为该结点对应的字符串  
* 每个结点的所有子结点路径代表的字符都不相同  
### 4、字典树的模板  
```
class Trie(object):
  
	def __init__(self): 
		self.root = {} 
		self.end_of_word = "#" 
 
	def insert(self, word): 
		node = self.root 
		for char in word: 
			node = node.setdefault(char, {}) 
		node[self.end_of_word] = self.end_of_word 
 
	def search(self, word): 
		node = self.root 
		for char in word: 
			if char not in node: 
				return False 
			node = node[char] 
		return self.end_of_word in node 
 
	def startsWith(self, prefix): 
		node = self.root 
		for char in prefix: 
			if char not in node: 
				return False 
			node = node[char] 
		return True
```
### 5、常见问题解法  

## 二、并查集  
### 1、适用场景  
* 组团、配队问题，即判断两个个体是否是一个群组的问题  
### 2、并查集的基本操作  
* makeSet(s)：建立一个新的并查集，其中包含s个单元素集合  
* unionSet(x,y)：把元素x和元素y所在的集合合并，要求x和y所在的集合不相交，如果相交则不合并  
* find(x):找到元素x所在的集合的代表，该操作也可以用于判断两个元素是否位于同一个集合，只要将他们各自的代表比较一下就可以了  
### 3、并查集的代码模板  
```
def init(p): 
	# for i = 0 .. n: p[i] = i; 
	p = [i for i in range(n)] 
 
def union(self, p, i, j): 
	p1 = self.parent(p, i) 
	p2 = self.parent(p, j) 
	p[p1] = p2 
 
def parent(self, p, i): 
	root = i 
	while p[root] != root: 
		root = p[root] 
	while p[i] != i: # 路径压缩 ?
		x = i; i = p[i]; p[x] = root 
	return root
```

## 三、高级搜索  
*相对朴素搜索的优化方向：不重复、剪枝* 
### 1、剪枝  
* 在对状态树进行搜索时，将一些已计算或一些不够好的节点进行剪枝，从而提升搜索效率  
### （1）常见问题解法  

### 2、双向BFS  
* 思路：从根结点和叶子结点同时开始进行BFS搜索，当结点重合时即完成搜索，最短步数即为左右步数之和  
### （1）常见问题解法  
* 
### 3、启发式搜索  
* 基于BFS搜索，在代码实现过程中使用优先队列来代替队列以实现一定程度的智能化  
* 启发式搜索代码模板  
```
def AstarSearch(graph, start, end):
	pq = collections.priority_queue() # 优先级 —> 估价函数（用以评价哪些结点最有希望是需要查找的结点）  
	pq.append([start]) 
	visited.add(start)
	while pq: 
		node = pq.pop() # 加入智能
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
   unvisited = [node for node in nodes if node not in visited]
		pq.push(unvisited)
```
### （1）常见问题解法  
*  

## 四、AVL和红黑树（基于二叉搜索树）  
*平衡二叉树：左右子树结点平衡* 
### 1、AVL树（属于平衡二叉树）  
* AVL树的来源：提升查找效率，因为二叉搜索树的时间复杂度仅与其深度有关，和结点个数无关  
* AVL树：  
（1） 平衡因子：左子树的高度 - 右子树的高度 / 右子树的高度 - 左子树的高度  若平衡则平衡因子取值仅有{-1，0,1}  
（2） 通过旋转操作来进行平衡  
* 左旋：右-右子树 --> 平衡  
* 右旋：左-左子树 --> 平衡  
* 左右旋：左-右子树 --> 左-左子树 --> 平衡  
* 右左旋：右-左子树 --> 右-右子树 --> 平衡  
* 当旋转的结点本身存在左右子树时，需要将对应的子树移动到相邻结点上成为其子树（例：当右旋结点存在右子树时，需要将该右子树移动到相邻结点上成为该结点的左子树）  
* 不足：结点需要存储额外信息、且调整次数频繁  
### 2、红黑树（属于近似平衡二叉树）  
* 每个结点要么是红色、要么是黑色  
* 根节点是黑色  
* 每个叶结点（NIL结点、空结点）是黑色的  
* 不能有相邻接的两个红色结点  
* 从任一结点到其每个叶子的所有路径都包含相同数目的黑色结点（确保任何一个结点的左右子树的高度差小于两倍）  
* 与AVL树的对比：  
（1） AVL树比红黑树的查找效率更高，因为AVL树的平衡性更严格  
（2） 红黑树的插入删除操作比AVL树效率更高，因为红黑树所需的旋转操作更少  
（3） AVL树每个结点需要存储平衡因子，红黑树每个结点每个结点只需要1bit，所以AVL树更耗内存  
（4） 当查询操作比较多时用AVL树，插入删除操作比较多时用红黑树    
