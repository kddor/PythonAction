# -*- coding:utf-8 -*-
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#定义链表
class LinkedList:
    def __init__(self):
        """
        Linked list 的初始化
        """
        self.length = 0
        self.head = None

    def is_empty(self):
        """
        判断该链表是否为空
        :return: boolean
        """
        return self.length == 0

    def append(self, this_node):
        """
        在链表末添加node/值,如果是node对象直接添加，否则先转换为node对象
        :param this_node: 数据或者node对象
        :return: None
        """
        if isinstance(this_node, Node):
            pass
        else:
            this_node = Node(data=this_node)
        if self.is_empty():
            # 链表为空的情况将头指针指向当前node
            self.head = this_node
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = this_node
        self.length += 1

    def FindKthToTail(self, head, k):
        front = head
        later = head
        for i in range(k):
            if front==None:
                return
            if front.next == None and i==k-1:
                return head
            front = front.next
        while front.next != None:
            front = front.next
            later = later.next
        return later.next

if __name__ == '__main__':
    #node1=ListNode(val='1')
    list=LinkedList()
    for i in range(10):
        list.append(i)
    head=list.head
    print(head)

    k=list.FindKthToTail(head,2)
    print(k)
