'''
����һ�ö��������������ö���������ת����һ�������˫������Ҫ���ܴ����κ��µĽ�㣬ֻ�ܵ������н��ָ���ָ��
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.root=TreeNode(-1)
        self.p=self.root
    def Convert(self, pRootOfTree):
        # write code here
        '''
        ����Ϊ˫��������left�䵱pre,right�䵱next
        (����ѡ���������)
        '''
        if not pRootOfTree:
            return None
        #if  not self.p:
         #   self.root=pRootOfTree
          #  self.p=pRootOfTree
        
        self.Convert(pRootOfTree.left)
        self.p.right=pRootOfTree
        pRootOfTree.left=self.p
        self.p=pRootOfTree
        self.Convert(pRootOfTree.right)
        self.root.right.left=None
        return self.root.right
        '''
        if not pRootOfTree:
            return None
        l=[]
        res=[]
        while pRootOfTree or len(l)!=0:
            while pRootOfTree:
                l.append(pRootOfTree)
                pRootOfTree=pRootOfTree.left
            pRootOfTree=l.pop()
            res.append(pRootOfTree)
            pRootOfTree=pRootOfTree.right
        for i in range(len(res)-1):
            res[i].right=res[i+1]
            res[i+1].left=res[i]
        return res[0]
'''