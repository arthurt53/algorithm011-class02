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
*基础元素：Value（Node）、Next（指针）*  
* 查询Node（时间复杂度O(n)）：  
* 新增Node（时间复杂度O(1)）：  
* 删除Node（时间复杂度O(1)）：  


### 3、跳表（Skip list）  
## 二、高级一维数据结构  
### 1、栈（Stack）  
### 2、队列（queue）  
### 3、优先队列（Array）  
### 4、双端队列（Array）  
