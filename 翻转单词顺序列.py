# -*- coding:utf-8 -*-
'''
ţ���������һ����Ա��Fish��ÿ���糿���ǻ�����һ��Ӣ����־��дЩ�����ڱ����ϡ�ͬ��Cat��Fishд�������ĸ���Ȥ����һ������Fish������������ȴ������������˼�����磬��student. a am I������������ʶ������һ�ԭ���Ѿ��ӵ��ʵ�˳��ת�ˣ���ȷ�ľ���Ӧ���ǡ�I am a student.����Cat��һһ�ķ�ת��Щ����˳��ɲ����У����ܰ�����ô��
'''
class Solution:
    def ReverseSentence(self, s):
        # write code here

        if s.strip()=="":
            return s
        l=list(s.split())
        length=len(l)
        #if length==0:
         #   return ""
        for i in range(length/2):
            temp=l[i]
            l[i]=l[length-1-i]
            l[length-i-1]=temp
        return ' '.join(str(i) for i in l)