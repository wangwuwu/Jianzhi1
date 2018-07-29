# -*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None:
            return None
        a=[]
        p=head
        while p!=None:
            a.append(p)
            p=p.next
        if k>len(a) or k==0:return None
        return a[-k]
    '''
    第二中思路是：有两个指针p、p，其中两者相差k个，当p达到最后一个时，q为倒数第k个
    '''