# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        '''
        �ɷ�����֪���������˷�������ĳ˻�ҪС���м�ģ����Բ������ҼбƷ�
        ��ʱ�Ҽ���Сʱ��ӣ����Ա�֤�˻���С�����ҵ�
        '''
        start=0
        end=len(array)-1
        while start<end :
            if array[start]+array[end]<tsum:
                start+=1
            if array[start]+array[end]>tsum:
                end-=1
            if array[start]+array[end]==tsum:
                return array[start],array[end]
        return []