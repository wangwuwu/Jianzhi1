# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, head):
        # write code her
        '''
        1).三个链表，分表存放节点，节点的random值，节点的Label，他们的位置是相互对应的
        2.）获得random节点在nodelist中的索引值
        3.）复制nodelist
        4.）根据random在nodelist中的位置，赋值nodelist的 random
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
            nodeList = []     #存放各个节点
        randomList = []   #存放各个节点指向的random节点。没有则为None
        labelList = []    #存放各个节点的值
        while head:
            randomList.append(head.random)
            nodeList.append(head)
            labelList.append(head.label)
            head = head.next
        #random节点的索引，如果没有则为-1   
        labelIndexList = map(lambda c: nodeList.index(c) if c else -1, randomList)
        dummy = RandomListNode(0)
        pre = dummy
        #节点列表，只要把这些节点的random设置好，顺序串起来就ok了。
        nodeList=map(lambda c:RandomListNode(c),labelList)
        #把每个节点的random绑定好，根据对应的index来绑定
        for i in range(len(nodeList)):
            if labelIndexList[i]!=-1:
                nodeList[i].random=nodeList[labelIndexList[i]]
        for i in nodeList:
            pre.next=i
            pre=pre.next
        return dummy.next
    '''