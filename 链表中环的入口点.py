# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        l=[]
        p=pHead
        while p:
            if p not in l:
                l.append(p)
                p=p.next
            else:
                return p
        return None