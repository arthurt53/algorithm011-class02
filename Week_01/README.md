# 第一周学习笔记  
## 一、基础一维数据结构  
### 1、数组（Array）  
* 调用/新建：  
`Array_list = []`   
* 查询（时间复杂度O(1)）：  
```  
Array_list[n] #查询第n个元素  
Array_list[a:b] #查询第a个元素到第b个元素  
```  
* 插入（时间复杂度O(n)）：  
```  
Array_list.insert(index,obj) #在index的位置插入obj元素  
Array_list.append(obj) #在最后添加obj元素（此时时间复杂度为O(1)）  
```
* 删除（时间复杂度O(n)）：  
```  
Array_list.remove(obj) #移除obj元素的第一个匹配项  
Array_list.pop([index = -1]) #移除index位置的元素（默认最后一个元素），并且返回该元素的值  
del(Array_list[n]) #删除索引位为n的元素  
```  
### 2、链表（Linked list）  
*适用场景：当需要频繁对数组进行修改操作时*  
*基础元素：Node-Value、Next；head；tail；None*  
* 新建Node：  
```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#实例化
node = Node(3)
```
* 新建链表：  
```
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
#实例化
link_list = LinkedList()
```
* 新增Node（时间复杂度O(1)）：
```
def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
#示例
link_list = LinkedList() #新建一个空的链表
link_list(append(3)) #给第一个节点赋值3
link_list(append(4)) #新增第二个节点并赋值4
```
* 查询Node（时间复杂度O(n)）：  

* 删除Node（时间复杂度O(1)）：  


### 3、跳表（Skip list）  
*适用场景：当链表中的元素有序时*  
**对标的是平衡树和二分查找，可以用来代替平衡树，缺点是维护成本较高，每增加删除一个元素就要把所有的索引都更新一遍**  
* 加速的关键：升维（增加多级索引）、以空间（O（n））换时间（O（log n））  
* 查询Node（时间复杂度O(log n)）：  
* 新增Node（时间复杂度O(log n)）：  
* 删除Node（时间复杂度O(log n)）：  
## 二、高级一维数据结构  
### 1、栈（Stack）  
### 2、队列（queue）  
### 3、优先队列（Array）  
### 4、双端队列（Array）  
