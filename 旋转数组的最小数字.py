'''
��һ�������ʼ�����ɸ�Ԫ�ذᵽ�����ĩβ�����ǳ�֮Ϊ�������ת�� ����һ���Ǽ�����������һ����ת�������ת�������СԪ�ء� ��������{3,4,5,1,2}Ϊ{1,2,3,4,5}��һ����ת�����������СֵΪ1�� NOTE������������Ԫ�ض�����0���������СΪ0���뷵��0
'''
# -*- coding:utf-8 -*-
'''
���ֲ��ҵĺ����ǣ�ԭ�������򣨷ǵݼ���������ת���һ�����ݴ��ڵڶ����ֵ��������ݣ���һ�����ݴ���arrau[0]ʱ˵����϶��ڵ�һ�����У���Ӧ��ѡȡ�������֮��Ĳ���
'''
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray)==0:
            return 0
        length=len(rotateArray)
        i=0
        j=length-1
        while i<j:
            mid=(i+j)/2
            if rotateArray[mid]>rotateArray[i]:
                i=mid#�����������ָ��Ԫ�ص�mid+1
            elif rotateArray[mid]==rotateArray[i]:
                return rotateArray[mid+1]
            else:
                j=mid