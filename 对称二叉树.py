# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        '''
        ʹ�ò�α������ж�ÿһ���ǲ��ǶԳƵ�,�����֤�˷��������⣬����ԳƲ�һ���Ǿ���Գ�'''
        if not pRoot:
            return True
        l=[]
        l.append(pRoot)
        flag=1
        while len(l)>0:
            counts=len(l)#ÿһ��Ľڵ����
            flag=self.duiC(l[:counts])
            if not flag:
                return False
            while counts>0:
                temp=l.pop(0)
               # if not temp:
                #    l.append(None)
                 #   l.append(None)
                if temp and temp.left:
                    l.append(temp.left)
                if temp and not temp.left:
                    l.append(None)
                if temp and temp.right:
                    l.append(temp.right)
                if temp and not temp.right:
                    l.append(None)
                counts-=1
        return flag
                
    def duiC(self,arr):#�ж������Ƿ�Գ�
        l=len(arr)
        for i in range(l/2):
            if (not arr[i] and  arr[l-i-1]) or ( arr[i] and not arr[l-i-1]):
                return False
            if arr[i] and arr[l-i-1] and arr[i].val!=arr[l-i-1].val:
                return False
        return True
