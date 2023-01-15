class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next


class linkedlistheap :
    def __init__(self):
        self.root = 0
        self.head = None
    
    #判断是否为空
    def is_empty(self):
        return self.head is None
    
    #添加元素
    def listcreate(self,new_data):
        new_node=Node(new_data)
        if self.is_empty():
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    #索引具体i的位置
    def locate(self,i):
        if i < 0 or i >= self.length():
            return None
        current_node=self.head
        index = 0
        while current_node and index != i :
            current_node = current_node.next
            index += 1
        return current_node

    def search(self, key):
        found = False
        if self.is_empty():
            return found
        else:
            current = self.head
            index = 0
            while current is not None and not found:
                if current.key == key:
                    found = True
                else:
                    current = current.next
                    index +=1
        return index

    #寻找父子
    def search_parent(self,i):
        return (i-1)//2
    def search_left(self,i):
        return 2 * i + 1
    def search_right(self,i):
        return (i + 1)*2

    #确定长度
    def length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    #交换位置
    def switch(self, k,l):
        node1 = self.locate(k)
        node2 = self.locate(l)
        node1.key, node2.key = node2.key, node1.key

    #形成最小堆
    def formheap(self):
        len = self.length()
        oper_index = len-1
        while oper_index > 0:
            cur_index = oper_index
            while cur_index >= 1:
                cur_node = self.locate(cur_index)
                parent_index = self.search_parent(cur_index)
                parent_node = self.locate(parent_index)
                cur_node_data = cur_node.key
                parent_node_data = parent_node.key

                if cur_node_data < parent_node_data:
                    self.switch(cur_index,parent_index)
                    cur_index = parent_index
                else:
                    break
            oper_index = oper_index -1
    #打印当前链表
    def print(self):
        for i in range(self.length()):
            cur_node = self.locate(i)
            print(cur_node.key,cur_node.next)
        print("   ")


            
    #插入功能
    def insert(self, key):
        self.listcreate(key)
        len = self.length()
        cur_index = len-1
        while cur_index >= 1:
                cur_node = self.locate(cur_index)
                parent_index = self.search_parent(cur_index)
                parent_node = self.locate(parent_index)
                cur_node_data = cur_node.key
                parent_node_data = parent_node.key
                if cur_node_data < parent_node_data:
                    self.switch(cur_index,parent_index)
                    cur_index = parent_index
                else:
                    break        

    #删除最小值功能  
    def delmin(self):
        len = self.length()
        last_node = Node(self.locate(len))
        min_node = Node(self.locate(0))
        self.root = last_node
        last_node.next = min_node.next
        self.formheap()
        return min_node.key

heap = linkedlistheap()
heap.listcreate(23)
heap.listcreate(31)
heap.listcreate(33)
heap.listcreate(14)
heap.listcreate(19)
heap.listcreate(7)
heap.formheap()

parent=heap.search_parent(4)
parent = heap.locate(parent)
print(parent.key)
left_child = heap.search_left(1)
left = heap.locate(left_child)
print(left.key)
right_child = heap.search_right(1)
right = heap.locate(right_child)
print(right.key)

heap.insert(20)
heap.print()
min_val = heap.delmin()
print(min_val.key)

from graphviz import Digraph

g = Digraph('result_picture',format='png')
i = 0
while i < heap.length():
    val = heap.locate(i).key
    g.node(name= str(val))
    i+=1
i=0
while i < heap.length():
    left_index = heap.search_left(i)
    right_index = heap.search_right(i)
    if left_index < heap.length():
        cur_index = heap.locate(i).key
        left_one = heap.locate(left_index).key
        g.edge(str(cur_index),str(left_one))
    else:
        break
    if right_index < heap.length():
        cur_index = heap.locate(i).key
        right_one = heap.locate(right_index).key
        g.edge(str(cur_index),str(right_one))
    else:
        break
    i+=1

g.view()