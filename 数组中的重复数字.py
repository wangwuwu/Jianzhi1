# -*- coding:utf-8 -*-
from collections import Counter
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
            dic = {}
            for i in range(len(numbers)):
                if numbers[i] not in dic:
                        dic[numbers[i]] = [i, 1]
                else:
                        dic[numbers[i]][1] += 1
            print(dic,'-----')
            fdic = list(filter(lambda x: x[1][1] > 1,dic.items()))
            if len(fdic)==0:
                return False
            print(fdic,'+++++++')
            fdic = sorted(fdic, key=lambda x: x[1][0])
            duplication[0] = fdic[0][0]
            return True