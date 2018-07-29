# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        flag=False
        if pRoot1 is None or pRoot2 is None:
            return flag
        if pRoot1.val==pRoot2.val:
            flag=self.t1Hast2(pRoot1,pRoot2)
        if flag is False:
            flag=self.HasSubtree(pRoot1.left,pRoot2)
        if flag is False :
            flag=self.HasSubtree(pRoot1.right,pRoot2)
        return flag
    def t1Hast2(self,t1,t2):
            if t2 is None:
                return True
            if t1 is None:
                return False
            if t1.val!=t2.val:
                return False
            return self.t1Hast2(t1.left,t2.left) and self.t1Hast2(t1.right,t2.right)