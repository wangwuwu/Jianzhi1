# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        '''
        ����Ŀ��֪���ӵ�һ����ͬ��֮�󣬼�Ϊͬһ����Y�Σ���������ʣ�µĽڵ㣬p1�ĳ�Ϊlen1,p2�ĳ�Ϊlen2������l1>l2��len1-len2=c,
        ��p1�ӵ�c����p2�ӵ�0����ʼ�������Ƚ��Ƿ��ǹ�ͬ�Ľ��
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
            #p2�Ƚ϶�
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
            ��������
            ��Ϊ������������󼸸���㣬���Խ���������洢�������Ӻ���ǰ���������һ����ͬ�ļ�Ϊ��һ���������
            '''
