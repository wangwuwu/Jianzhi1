'''
����ĳ��������ǰ���������������Ľ�������ؽ����ö����������������ǰ���������������Ľ���ж������ظ������֡���������ǰ���������{1,2,4,7,3,5,6,8}�������������{4,7,2,1,5,3,8,6}�����ؽ������������ء�
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # ���ع����TreeNode���ڵ�
    '''
    �����Ĺ�����һ���ݹ����
    '''
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        rootT=self.reBuildTree(pre,tin)
        return rootT
    def reBuildTree(self,pre,tin):
        if not pre or not tin:
            return None
        root=TreeNode(pre.pop(0))
        index=tin.index(root.val)
        left=tin[0:index]
        right=tin[index+1:]
        root.left=self.reBuildTree(pre,left)
        root.right=self.reBuildTree(pre,right)
        return root