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
        方法一：递归
        方法二：求树的深度可考虑层次遍历
        '''
        
        #方法一
        if pRoot is None:
            return 0
        l=r=0
        if pRoot.left is not None:
           l=self.TreeDepth(pRoot.left)
        if pRoot.right is not None:
           r=self.TreeDepth(pRoot.right)
        return max(l,r)+1
        
        #使用list存储树节点
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
        非递归，好理解版本，每遍历完一层，depth+1，
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
            for i in range(size):#位于同一层的数据
                temp=l.pop(0)
                if temp.left is not None:
                    l.append(temp.left)
                if  temp.right is  not None:
                    l.append(temp.right)
        return depth
        '''