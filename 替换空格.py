'''
��ʵ��һ����������һ���ַ����е�ÿ���ո��滻�ɡ�%20�������磬���ַ���ΪWe Are Happy.�򾭹��滻֮����ַ���ΪWe%20Are%20Happy
'''
# -*- coding:utf-8 -*-
class Solution:
    # s Դ�ַ���
    def replaceSpace(self, s):
        # write code here
        a=[]
        for i in s:
            if i!=' ':
                a.append(i)
            else:
                a.append('%')
                a.append('20')
        return ''.join(a)