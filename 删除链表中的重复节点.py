# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        '''
        ������Ҫ���Ǽ����������1.���нڵ�val��ȣ���Ϊ�����������,���ж�ɾ����������һ���ڵ�����һ���ڵ��Ƿ���ȣ�������򷵻�None
        2.����󼸸��ڵ����ʱ��4555����ʱ��p2ָ��4��p3ָ��գ�Ӧ��p2���ɾ��
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