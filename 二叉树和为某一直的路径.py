# -*- coding:utf-8 -*-
import math
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    '''
    1.这里使用树的深度优先遍历
    2.在深度遍历的时候，有连个列表l,path，l存放每次遍历的节点，当遍历到叶子节点且和为expectNumber时候，将l存放到path中，同时l回退一个节点即pop
    3.此在每一次递归没有返回值，而是每一层递归对l,和path操作，当递归全部完成时返回path
    '''
    def __init__ (self):
        self.l = []
        self.path = []
    def FindPath(self, root, expectNumber):
        if root is None:
            return []
        self.dfs(root,expectNumber)
        return self.path
    def dfs(self,root,expectNumber):
        if not root:
            return None
        expectNumber-=root.val
        self.l.append(root.val)
        if expectNumber==0 and root.left is None and root.right is None:
            self.path.append([x for x in self.l])
        if root.left:
            self.dfs(root.left,expectNumber)
        if root.right:
            self.dfs(root.right,expectNumber)
        self.l.pop()#遍历到叶子节点时回退到父节点
