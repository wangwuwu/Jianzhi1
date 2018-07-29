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
        使用层次遍历，判断每一层是不是对称的,最后验证此法存在问题，数组对称不一定是镜像对称'''
        if not pRoot:
            return True
        l=[]
        l.append(pRoot)
        flag=1
        while len(l)>0:
            counts=len(l)#每一层的节点个数
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
                
    def duiC(self,arr):#判断数组是否对称
        l=len(arr)
        for i in range(l/2):
            if (not arr[i] and  arr[l-i-1]) or ( arr[i] and not arr[l-i-1]):
                return False
            if arr[i] and arr[l-i-1] and arr[i].val!=arr[l-i-1].val:
                return False
        return True
