# -*- coding:utf-8 -*-
from collections import Counter
class Solution:
    # ����[a,b] ����ab�ǳ���һ�ε���������
    def FindNumsAppearOnce(self, array):
        # write code here
        '''
        #����һ��ʹ��counter����
        dic=Counter(array)
        res=[]
        for i in dic:
            if dic[i]==1:
                res.append(i)
        return res
        '''
        #�����������ⷨ-ǰ�᣺������ͬ�������Ϊ0��һ������0���Ϊ����
        #�����������ݽ������ȡΪһ�����λ�����մ�λ�����ݻ���Ϊ�������飬����������򼴿ɷֱ�õ�������
        if len(array)==1:
            return []
        temp=0
        for i in array:#��һ�����
            temp^=i
        index=0#Ϊ1�����λ
        while (temp & 1)==0:#ȡ���һλ��1��
            temp>>=1
            index+=1
        a=b=0
        for i in array:
            if self.IsOne(i,index):
                a^=i
            else:
                b^=i
        return a,b
    def IsOne(self,data,k):#�ж����ĵ�kλ�Ƿ�Ϊ1
        data=data>>k
        return data & 1