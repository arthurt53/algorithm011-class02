# 第八周学习笔记  
## 一、位运算  
*优势：速度快*
### 1、位运算符  
* 左移：<< （ex：0011 << 0110）  
* 右移：>> （ex：0110 >> 0011）  
* 按位或：   |  （ex：0110 | 0011 = 0111）  
* 按位与：   &  （ex：0110 & 0011 = 0010）  
* 按位取反： ~  （ex：~ 0110 = 1001）  
* 按位异或： ^  （ex：0110 ^ 0011 = 0101）  
*异或性质：  
（1） x ^ 0 = x  
（2） x ^ 1s = ~x  
（3） x ^ (~x) = 1s  
（4） x ^ x = 0  
（5） c = a ^ b => a = c ^ b , b = c ^ a
（6） a ^ b ^ c = (a ^ b) ^ c = a ^ (b ^ c)*  
### 2、指定位置的位运算  
* 将x最右边的n位清零：x & (~ 0 << n)  
* 获取x的第n位值（0或1）： (x >> n) & 1  
* 获取x的第n位的幂值： x & (1 << n)  
* 仅将第n位置为1：x | (1 << n)  
* 仅将第n为置为0：x & (~(1 << n))  
* 将x最高位至第n位（含）清零： x & ((1 << n) -1)   
### 3、实战位运算要点  
* 判断奇偶： 奇：( x & 1 ) == 1 偶：( x & 1 ) == 0  
* x >> 1 --> x / 2  
* x = x & (x -1) 清零最低位的1  
* x & -x 得到最低位的1  
* x & ~x = 0  
### 4、常见问题的解法  
* 位 1 的个数  
```
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            n &= (n - 1)
            count += 1
        return count
```
* 2 的幂  
```
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0
```
* 颠倒二进制位  
```
def reverseBits(self , n):
    ans , MASK = 0, 1

    for i in range(32):
        if n & MASK:
            ans |= 1 << (31 - i)
        MASK <<= 1

    return ans
```

## 二、布隆过滤器  
*类似于哈希表，但布隆过滤器实现的是模糊查询*  
### 1、基础概念  
* 由一个很长的二进制向量和一系列随机映射函数构成  
* 布隆过滤器可以用于检索一个元素是否在一个集合中  
### 2、优缺点  
* 优点：空间效率和查询时间都远远超过一般算法  
* 缺点：有一定的误识别率和删除困难  
### 3、原理  
* 分别给 { x, y, z} 三个元素分配n个二进制位， 将这些二进制位的并集进行保存， 若查询值的二进制位中有0，则该查询值必不在集合中；若均为1，则该查询值有可能在集合中  
* 示例：  
![image](https://github.com/arthurt53/Graph_hub/blob/master/QQ%E5%9B%BE%E7%89%8720200816145435.png)  
### 4、应用  
* 比特币网络  
* 分布式系统（Map-Reduce）  
* Redis缓存  
* 垃圾邮件、评论等的过滤  
### 5、实现代码  
```
from bitarray import bitarray 
import mmh3 
class BloomFilter: 
	def __init__(self, size, hash_num): 
		self.size = size 
		self.hash_num = hash_num 
		self.bit_array = bitarray(size) 
		self.bit_array.setall(0) 
    
	def add(self, s): 
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			self.bit_array[result] = 1 
      
	def lookup(self, s): 
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			if self.bit_array[result] == 0: 
				return "Nope" 
		return "Probably" 
    
bf = BloomFilter(500000, 7) 
bf.add("dantezhao") 
print (bf.lookup("dantezhao")) 
print (bf.lookup("yyj")) 
```
## 三、LRU Cache（缓存）  
### 1、基础概念  
* 两个要素：大小、替换策略 - Least Recently Used    
* 实现方法：Hash table + Double LinkedList  
* 复杂度：O(1)查询 O(1) 修改、更新  
* 其他替换策略： LFU - Least Frequently Used等  
### 2、实现代码  
```
class LRUCache(object): 

	def __init__(self, capacity): 
		self.dic = collections.OrderedDict() 
		self.remain = capacity

	def get(self, key): 
		if key not in self.dic: 
			return -1 
		v = self.dic.pop(key) 
		self.dic[key] = v   # key as the newest one 
		return v 

	def put(self, key, value): 
		if key in self.dic: 
			self.dic.pop(key) 
		else: 
			if self.remain > 0: 
				self.remain -= 1 
			else:   # self.dic is full
				self.dic.popitem(last=False) 
		self.dic[key] = value
    
 # 哈希表+双向链表实现
 class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部和伪尾部节点    
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果 key 存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
    
    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node
```
## 四、排序算法  
### 1、常用排序算法  
（1） 比较类排序：通过比较来决定元素间的相对次序，时间复杂度最低为O(nlogn）  
* 交换排序：冒泡排序 O(n^2)、快速排序 O(nlogn)  
*冒泡排序：嵌套循环，每次查看相邻的元素如果逆序，则交换*  
*快速排序：数组取标杆piovt，将小元素放在piovt左边，大元素放右侧，然后依次对左边和右边的子数组继续快排，以达到整个序列有序*  
* 插入排序：简单插入排序 O(n^2)、希尔排序 O(n^1.3)   
*简单插入排序：从前往后逐步构建有序数组；对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入*  
* 选择排序：简单选择排序 O(n^2)、堆排序 O(nlogn)   
*简单选择排序：每次找到最小值，然后放在待排序数组的起始位置*  
*堆排序：数组元素依次建立小顶堆，依次取堆顶元素，并删除*  
* 归并排序O(nlogn)：二路归并排序、多路归并排序  
*a、把长度为n的输入序列分成两个长度为n/2的子序列*  
*b、对两个子序列分别采用归并排序*  
*c、将两个排序好的子序列合并成一个最终的排序序列*  
（2） 非比较累排序：不通过比较来决定元素间的相对次序，可以突破基于比较排序的时间下界，以线性时间运行，一般只能用于整形的元素  
* 计数排序：计数排序要求输入的数据必须是有确定范围的整数。将输入的数据值转化为键存储在额外开辟的数组空间中；然后依次把计数大于 1 的填充回原数组  
* 桶排序：假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排  
* 基数排序：按照低位先排序，然后收集；再按照高位排序，然后再收集；依次类推，直到最高位。有时候有些属性是有优先级顺序的，先按低优先级排序，再按高优先级排序   
### 2、常用排序代码  
* 快速排序：  
```
def quick_sort(begin, end, nums):
    if begin >= end:
        return
    pivot_index = partition(begin, end, nums)
    quick_sort(begin, pivot_index-1, nums)
    quick_sort(pivot_index+1, end, nums)
    
def partition(begin, end, nums):
    pivot = nums[begin]
    mark = begin
    for i in range(begin+1, end+1):
        if nums[i] < pivot:
            mark +=1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark
```
* 归并排序：  
```
def mergesort(nums, left, right):
    if right <= left:
        return
    mid = (left+right) >> 1
    mergesort(nums, left, mid)
    mergesort(nums, mid+1, right)
    merge(nums, left, mid, right)

def merge(nums, left, mid, right):
    temp = []
    i = left
    j = mid+1
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i +=1
        else:
            temp.append(nums[j])
            j +=1
    while i<=mid:
        temp.append(nums[i])
        i +=1
    while j<=right:
        temp.append(nums[j])
        j +=1
    nums[left:right+1] = temp
```
* 堆排序：  
```
def heapify(parent_index, length, nums):
    temp = nums[parent_index]
    child_index = 2*parent_index+1
    while child_index < length:
        if child_index+1 < length and nums[child_index+1] > nums[child_index]:
            child_index = child_index+1
        if temp > nums[child_index]:
            break
        nums[parent_index] = nums[child_index]
        parent_index = child_index
        child_index = 2*parent_index + 1
    nums[parent_index] = temp


def heapsort(nums):
    for i in range((len(nums)-2)//2, -1, -1):
        heapify(i, len(nums), nums)
    for j in range(len(nums)-1, 0, -1):
        nums[j], nums[0] = nums[0], nums[j]
        heapify(0, j, nums)
```
* 冒泡排序：  
```
def bubble_sort(nums):

    for i in range(len(nums) - 1):  
        ex_flag = False  
        for j in range(len(nums) - i - 1):  
            
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                ex_flag = True
        if not ex_flag:
            return nums  
	    
    return nums  
```
* 选择排序：  
```
def selection_sort(arr):
	for i in range(len(arr) - 1):
		min_index = i
		for j in range(i + 1, len(arr)):
        		if arr[j] < arr[min_index]:
                		min_index = j
		arr[min_index], arr[i] = arr[i], arr[min_index]
	return arr
```
* 插入排序：  
```
def insertionSort(arr): 
  
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
```
### 3、常见问题的解法  
* 数组的相对排序  
```
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        in_arr2 = []
        not_in_arr2 = []
        Hash = {}
        for i in arr1:
            Hash[i] = Hash.get(i, 0) + 1
        arr1 = set(arr1)
        for j in arr1:
            if j not in arr2:
                not_in_arr2 += [j]*Hash[j]
        not_in_arr2.sort()
        for k in arr2:
            in_arr2 += [k]*Hash[k]
        return in_arr2+not_in_arr2
```
* 合并区间  
```
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort()
        res = [intervals[0]]
        for x, y in intervals[1:]:
            if res[-1][1] < x:
                res.append([x, y])
            else:
                res[-1][1] = max(y, res[-1][1])
        return res
```
