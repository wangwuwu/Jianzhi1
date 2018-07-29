# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # ·µ»ØListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead is None:
            return None
        pre=next=None
        while pHead:
            next=pHead.next
            pHead.next=pre
            pre=pHead
            pHead=next
        return pre