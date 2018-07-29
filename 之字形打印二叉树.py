# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        self.res=[]
        l=[]
        if not pRoot:
            return ""
        l.append(pRoot)
        k=0#表层数
        while len(l)>0:
            k+=1
            counts=len(l)#每一层的节点数
            temparr=[0]*counts
            lenght=counts
            while counts:
                temp=l.pop(0)
                if k%2==0:
                    temparr[counts-1]=temp.val
                else:
                    temparr[lenght-counts]=temp.val
                if temp.left:
                    l.append(temp.left)
                if temp.right:
                    l.append(temp.right)
                counts-=1
            self.res.append(temparr)
                
        return self.res
