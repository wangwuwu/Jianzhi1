# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # ���ؾ������ĸ��ڵ�
    def Mirror(self, root):
        # write code here
        if root is not None:
            temp=root.left
            root.left=root.right
            root.right=temp
            self.Mirror(root.left)
            self.Mirror(root.right)
        return root