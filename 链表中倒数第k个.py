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
    �ڶ���˼·�ǣ�������ָ��p��p�������������k������p�ﵽ���һ��ʱ��qΪ������k��
    '''