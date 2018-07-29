# -*- coding:utf-8 -*-
from math import *
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        '''
        平衡二叉树判断标准：左右字树的深度差不超过1
        对任意节点a,判断以此为根节点的树是否是平衡二叉树；对树中所有节点执行此操作
        此法可以优化;从下往上遍历，保证每个节点至多遍历一次
        '''
        if pRoot is  None:
            return 1
        ldepth=rdepth=0
        if pRoot.left is not None:
            ldepth=self.getTreeDepth(pRoot.left)
            self.IsBalanced_Solution(pRoot.left)
        if pRoot.right is not None:
            rdepth=self.getTreeDepth(pRoot.right)
            self.IsBalanced_Solution(pRoot.right)
        if abs(ldepth-rdepth)>1:
            return 0
        return 1
    def getTreeDepth(self,tree):
        if tree is None:
            return 0
        ldepth=rdepth=0
        if tree.left is not None:
            ldepth=self.getTreeDepth(tree.left)
        if tree.right is not None:
            rdepth=self.getTreeDepth(tree.right)
        return max(ldepth,rdepth)+1