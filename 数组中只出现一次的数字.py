# -*- coding:utf-8 -*-
from collections import Counter
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        '''
        #方法一：使用counter函数
        dic=Counter(array)
        res=[]
        for i in dic:
            if dic[i]==1:
                res.append(i)
        return res
        '''
        #方法二：异或解法-前提：两个相同的数异或为0，一个数与0异或为自身
        #将数组中数据进行异或，取为一的最低位，按照此位将数据划分为两个数组，在数组内异或即可分别得到两个数
        if len(array)==1:
            return []
        temp=0
        for i in array:#第一次异或
            temp^=i
        index=0#为1的最低位
        while (temp & 1)==0:#取最后一位和1与
            temp>>=1
            index+=1
        a=b=0
        for i in array:
            if self.IsOne(i,index):
                a^=i
            else:
                b^=i
        return a,b
    def IsOne(self,data,k):#判断数的第k位是否为1
        data=data>>k
        return data & 1