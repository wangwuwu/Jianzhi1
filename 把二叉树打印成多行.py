# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # ���ض�ά�б�[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        '''
        ����ʹ�ò�α���
        '''
        if not pRoot:
            return ""
        self.res=[]
        l=[]
        l.append(pRoot)
        while len(l):
            counts=len(l)
            temparr=[]
            while counts:
                temp=l.pop(0)
                temparr.append(temp.val)
                if temp.left:
                    l.append(temp.left)
                if temp.right:
                    l.append(temp.right)
                counts-=1
            self.res.append(temparr)
        return self.res
