# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.counts=0
        self.node=None
    def KthNode(self, pRoot, k):
        # write code here
        '''
        中序遍历下第K个
        '''
        if not pRoot:
            return None
        self.KthNode(pRoot.left,k)
        self.counts+=1
        if self.counts==k:
            self.node=pRoot
        self.KthNode(pRoot.right,k)
        return self.node
        #return None