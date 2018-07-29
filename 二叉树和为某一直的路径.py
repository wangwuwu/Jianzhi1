# -*- coding:utf-8 -*-
import math
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    '''
    1.����ʹ������������ȱ���
    2.����ȱ�����ʱ���������б�l,path��l���ÿ�α����Ľڵ㣬��������Ҷ�ӽڵ��Һ�ΪexpectNumberʱ�򣬽�l��ŵ�path�У�ͬʱl����һ���ڵ㼴pop
    3.����ÿһ�εݹ�û�з���ֵ������ÿһ��ݹ��l,��path���������ݹ�ȫ�����ʱ����path
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
        self.l.pop()#������Ҷ�ӽڵ�ʱ���˵����ڵ�
