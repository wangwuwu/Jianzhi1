# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # ���ش�β����ͷ�����б�ֵ���У�����[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        a = []
        if listNode is None:
           return a

        p = listNode
        while p != None:
            a.append(p.val)
            p = p.next
        return a[::-1]