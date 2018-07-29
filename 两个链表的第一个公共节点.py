# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        '''
        从题目可知，从第一个共同点之后，即为同一个表（Y形），即共用剩下的节点，p1的长为len1,p2的长为len2，假设l1>l2，len1-len2=c,
        则p1从第c个，p2从第0个开始遍历，比较是否是共同的结点
        '''
        p1=pHead1
        p2=pHead2
        len1=0
        len2=0
        while p1:
            len1+=1
            p1=p1.next
        while p2:
            len2+=1
            p2=p2.next
        p1=pHead1
        p2=pHead2
        if len1>len2:
            #p2比较短
            count=0
            while count<len1-len2:
                p1=p1.next
                count+=1
            while p1 and p2:
                if p1 is p2 :
                    return p1
                else:
                    p1=p1.next
                    p2=p2.next
        else:
            count=0
            while count<len2-len1:
                p2=p2.next
                count+=1
            while p1 and p2:
                if p1 is p2 :
                    return p1
                else:
                    p1=p1.next
                    p2=p2.next
            '''
            方法二：
            因为两个链表共用最后几个结点，可以将两个链表存储起来，从后往前遍历，最后一个相同的即为第一个公共结点
            '''
