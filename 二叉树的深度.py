# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        '''
        ����һ���ݹ�
        ����������������ȿɿ��ǲ�α���
        '''
        
        #����һ
        if pRoot is None:
            return 0
        l=r=0
        if pRoot.left is not None:
           l=self.TreeDepth(pRoot.left)
        if pRoot.right is not None:
           r=self.TreeDepth(pRoot.right)
        return max(l,r)+1
        
        #ʹ��list�洢���ڵ�
        '''
        if pRoot is None:
            return 0
        l=[]
        l.append(pRoot)
        depth=0
        counts=0
        layercounts=1
        while len(l)!=0:
            temp=l.pop(0)
            counts+=1
            if temp.left:
                l.append(temp.left)
            if temp.right:
                l.append(temp.right)
            if layercounts==counts:
                layercounts=len(l)
                counts=0
                depth+=1
        return depth
        '''
        '''
        �ǵݹ飬�����汾��ÿ������һ�㣬depth+1��
        '''
        '''
        if pRoot is None:
            return 0
        l=[]
        depth=0
        l.append(pRoot)
        while len(l)!=0:
            size=len(l)
            depth+=1
            for i in range(size):#λ��ͬһ�������
                temp=l.pop(0)
                if temp.left is not None:
                    l.append(temp.left)
                if  temp.right is  not None:
                    l.append(temp.right)
        return depth
        '''