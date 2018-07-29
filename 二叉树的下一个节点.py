# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
'''
class Solution:
    def GetNext(self, pNode):
        # write code here
        dummy = pNode
        while dummy.next:
            dummy = dummy.next
        self.result = []
        self.midTraversal(dummy)
        return self.result[self.result.index(pNode) + 1] if self.result.index(pNode) != len(self.result) - 1 else None
    def midTraversal(self, root):
        if not root: return
        self.midTraversal(root.left)
        self.result.append(root)
        self.midTraversal(root.right)
'''
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode or (pNode and not pNode.next and not pNode.left and not pNode.right):#空节点或者独立节点
            return None
        root=pNode
        while root.next:
            root=root.next
        self.nodes=[]
        self.midscan(root)
        index=self.nodes.index(pNode)
        return self.nodes[index+1] if index<len(self.nodes)-1 else None
    
    def midscan(self,node):
        if not node :
            return None
        self.midscan(node.left)
        self.nodes.append(node)
        self.midscan(node.right)
