# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # ���ش��ϵ���ÿ���ڵ�ֵ�б�����[1,2,3]
    '''
    ����ʹ������ʱ�б�q�����洢���нڵ㣬��˳��Ϊ���ڵ�pop�������ӽڵ���������������ԭ����˳��
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