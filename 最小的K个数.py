# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        sett=set(tinput)
        if len(sett)<k:
            return []
        arr=sorted(sett)
        return arr[:k]
    '''
    Ê¹ÓÃ¶ÑÅÅÐò
    '''