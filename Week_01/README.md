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
*基础元素：Node-Value、Next；head；tail；None（在Python中采用引用+类来实现）*  
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
        node = Node(data) #实例化一个节点
        if self.head is None:   #如果第一个指针指向None，说明这是链表添加的第一个元素，则首尾指针指向实例化的节点
            self.head = node
            self.tail = node
        else: #此时节点的next指针指向实例化的节点
            self.tail.next = node  #移动Next指针
            self.tail = node    #移动tail指针
#示例
link_list = LinkedList() #新建一个空的链表
link_list(append(3)) #给第一个节点赋值3
link_list(append(4)) #新增第二个节点并赋值4
```
* 插入Node（时间复杂度O(1)*将查找位置算进去时间复杂度是否为O(n)？*）：  
```
def insert(self, idx, value):
        cur = self.head
        cur_idx = 0
        if cur is None:         # 判断是否是空链表
            raise Exception('The list is an empty list')
        while cur_idx < idx-1:  # 遍历链表
            cur = cur.next
            if cur is None:     # 判断是不是最后一个元素
                raise Exception('list length less than index')
            cur_idx += 1
        node = Node(value)
        node.next = cur.next    #第一步，将新节点的next指针指向插入位置前节点的next指针指向的对象
        cur.next = node         #第二步，将插入位置前节点的next指针指向新节点
        if node.next is None:   
            self.tail = node
```
* 查询Node（时间复杂度O(n)）：  
```
def search(self, item):
        current = self.head
        found = False
        while current is not None and not found: #遍历链表
            if current.data == item:
                found = True
            else:
                current = current.next
        return found
```
* 删除Node（时间复杂度O(1)）：  
```
def remove(self, idx):
       cur = self.head
       cur_idx = 0
       if self.head is None:  # 空链表时
           raise Exception('The list is an empty list')
       while cur_idx < idx-1:  # 遍历链表
           cur = cur.next
           if cur is None:
               raise Exception('list length less than index')
           cur_idx += 1
       if idx == 0:   # 当删除第一个节点时
           self.head = cur.next     # 将head指针指向删除位置前节点next指针指向的对象
           cur = cur.next           
           return
       if self.head is self.tail:   # 当只有一个节点的链表时
           self.head = None
           self.tail = None
           return
       cur.next = cur.next.next #将删除位置前节点next指针指向的对象指向删除节点后一个节点next指针指向的对象
       if cur.next is None:  # 当删除的节点是链表最后一个节点时
           self.tail = cur      # 将tail指针指向删除节点前的一个节点
```
### 3、跳表（Skip list）  
*适用场景：当链表中的元素有序时（工程实例：LRU Cache、Redis）*  
**对标的是平衡树和二分查找，可以用来代替平衡树，缺点是维护成本较高，每增加删除一个元素就要把所有的索引都更新一遍**  
* 加速的关键：升维（增加多级索引）、以空间（O（n））换时间（O（log n））  
* 查询Node（时间复杂度O(log n)）/ 新增Node（时间复杂度O(log n)）/ 删除Node（时间复杂度O(log n)）

## 二、高级一维数据结构  
### 1、栈（Stack）  
* 特性：先入后出（可以用两个栈来实现队列的特性）  
* 添加/取出（时间复杂度O(1)）；查询（时间复杂度O(n)）  
### 2、队列（queue）  
* 特性：先入先出（可以用两个队列来实现栈的特性）  
* 添加/取出（时间复杂度O(1)）；查询（时间复杂度O(n)）  
### 3、优先队列（Priority Queue）  
* 特性：按一定的优先级出  
### 4、双端队列（Deque）  
* 特性：两端均可进出  
* 添加/取出（时间复杂度O(1)）；查询（时间复杂度O(n)）  
* 调用：  
`from collections import deque`
* 新建队列：  
`deque_test = deque('')  #新建一个空的双端队列`
* 添加元素：  
```
deque_test.append(X)        #在双端队列的右侧加入元素X
deque_test.appendleft(X)    #在双端队列的左侧加入元素X
deque_test.extend(Y)        #在双端队列的右侧加入可迭代元素Y
deque_test.extendleft(Y)    #在双端队列的左侧加入可迭代元素Y（如果可迭代元素为['1','2','3']，加入队列后为['3','2','1']）
```
* 取出/删除元素：  
```
deque_test.pop()        #在双端队列的右侧取出元素
deque_test.popleft()    #在双端队列的左侧取出元素
deque_test.remove(X)     #从双端队列的左侧删除第一次出现的元素X
```
* 查询：  
`deque_test[n]      #查询队列中索引号为n的元素`  
***
改写Deque代码  
```
from collections import deque

deque_test = deque('')
deque_test.appendleft('a')
deque_test.appendleft('b')
deque_test.appendleft('c')
print(deque_test)

str_test = deque_test[0]
print(str_test)
print(deque_test)

while len(deque_test) > 0:
    print(deque_test.popleft())
    
print(deque_test)
```
