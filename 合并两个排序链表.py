# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        '''
        1.检查输入是否为零的各种情况
        2.以较小的那个链表为基准，将另一个链表插入其中
        '''
        # write code here
        '''
        if pHead1 is None and pHead2 is None: return None
        if pHead1 is None :return pHead2
        if pHead2 is None :return pHead1
        if pHead1.val>pHead2.val:
            temp=pHead2
            pHead2=pHead1
            pHead1=temp
        temp1=pHead1
        temp11=temp1.next
        temp2=pHead2
        while pHead1 is not None and temp11 is not None  and pHead2 is not None:
            global temp1,temp2,temp11
            if temp1.val<=pHead2.val and temp11.val>pHead2.val:
                temp2=pHead2.next
                temp1.next=pHead2
                pHead2.next=temp11
                temp1=temp11
                temp11=temp11.next
                pHead2=temp2
            else:
                temp1=temp11
                temp11=temp11.next
        if pHead2 is not None:
            temp1.next=pHead2
        return pHead1
        '''
        if pHead1 is None:return pHead2
        if pHead2 is None: return pHead1
        if pHead1.val<=pHead2.val:
            pHead1.next=self.Merge(pHead1.next,pHead2)
            return pHead1
        else:
            pHead2.next=self.Merge(pHead1,pHead2.next)
            return pHead2
            