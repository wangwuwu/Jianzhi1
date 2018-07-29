# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        '''
        这里需要考虑几种特殊情况1.所有节点val相等，因为链表是有序的,可判断删除后的链表第一个节点和最后一个节点是否相等，若相等则返回None
        2.当最后几个节点相等时如4555，此时盘p2指向4，p3指向空，应将p2后的删除
        '''
        if  not pHead  or not pHead.next  :
            return pHead
        f=ListNode(999999999)
        k=pHead.val
        f.next=pHead
        pHead=f
        p2=pHead
        p3=p2.next
        flag=0
        while p3 and p3.next is not None:
            num=p3.val
            if p3.next.val==num:
                flag=1
                p3=p3.next
            if not flag  and p3.next and p3.next.val!=num:
                p2=p3
                p3=p3.next
                continue
            if flag and p3.next and p3.next.val!=num:
                p2.next=p3.next
                p3=p3.next
                flag=0
        if p2.next!=p3:
             p2.next=None

                
        return pHead.next if p3.val!=k  else None