# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    '''
    这里使用了临时列表q，来存储树中节点，其顺序为：节点pop，将其子节点加入进来，保存了原来的顺序
    '''
    def PrintFromTopToBottom(self, root):
        # write code here
        l=[]
        q=[]
        if root is None:
            return l
        q.append(root)
        while len(q)!=0:
            temp=q.pop(0)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            l.append(temp.val)
        return l