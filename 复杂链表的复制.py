# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # ���� RandomListNode
    def Clone(self, head):
        # write code her
        '''
        1).���������ֱ��Žڵ㣬�ڵ��randomֵ���ڵ��Label�����ǵ�λ�����໥��Ӧ��
        2.�����random�ڵ���nodelist�е�����ֵ
        3.������nodelist
        4.������random��nodelist�е�λ�ã���ֵnodelist�� random
        '''
        nodelist=[]
        randomlist=[]
        while head:
            nodelist.append(head)
            randomlist.append(head.random)
            head=head.next
        indexOfRandomInNodelist=[nodelist.index(x) if x else -1  for x in randomlist]
        nodelist=[RandomListNode(x.label) for x in nodelist]
        for i in range(len(nodelist)):
            if indexOfRandomInNodelist[i]!=-1:
                nodelist[i].random=nodelist[indexOfRandomInNodelist[i]]
        dummy=RandomListNode(0)
        pre=dummy
        for i in nodelist:
            pre.next=i
            pre=pre.next
        return dummy.next
    '''
            nodeList = []     #��Ÿ����ڵ�
        randomList = []   #��Ÿ����ڵ�ָ���random�ڵ㡣û����ΪNone
        labelList = []    #��Ÿ����ڵ��ֵ
        while head:
            randomList.append(head.random)
            nodeList.append(head)
            labelList.append(head.label)
            head = head.next
        #random�ڵ�����������û����Ϊ-1   
        labelIndexList = map(lambda c: nodeList.index(c) if c else -1, randomList)
        dummy = RandomListNode(0)
        pre = dummy
        #�ڵ��б�ֻҪ����Щ�ڵ��random���úã�˳��������ok�ˡ�
        nodeList=map(lambda c:RandomListNode(c),labelList)
        #��ÿ���ڵ��random�󶨺ã����ݶ�Ӧ��index����
        for i in range(len(nodeList)):
            if labelIndexList[i]!=-1:
                nodeList[i].random=nodeList[labelIndexList[i]]
        for i in nodeList:
            pre.next=i
            pre=pre.next
        return dummy.next
    '''