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
        ƽ��������жϱ�׼��������������Ȳ����1
        ������ڵ�a,�ж��Դ�Ϊ���ڵ�����Ƿ���ƽ������������������нڵ�ִ�д˲���
        �˷������Ż�;�������ϱ�������֤ÿ���ڵ��������һ��
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