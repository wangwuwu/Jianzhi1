# -*- coding:utf-8 -*-
from collections import Counter
class Solution:
    # ����Ҫ�ر�ע��~�ҵ������ظ���һ��ֵ����ֵ��duplication[0]
    # ��������True/False
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