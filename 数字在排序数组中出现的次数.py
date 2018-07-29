# -*- coding:utf-8 -*-
from collections import Counter
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        #return Counter(data)[k]
        #����һ��ʹ�ü�����
        #��������ֱ�ӱ���
        #����������ĿΪ�������飬�ɿ��Ƕ��ֲ���
        if len(data)==0:#����Ϊ��
            return 0
        index=self.binaryLooking(data,0,len(data)-1,k)
        if index==-1:#û�ҵ�
            return 0
        print('index:',index)
        p1=p2=index
        counts=0
        while data[p1]==k and p1>=0:
            counts+=1
            p1-=1
        while p2<=len(data)-1 and data[p2]==k:
            counts+=1
            p2+=1
        return counts-1

    def binaryLooking(self,arr,i,j,k):
        # if i==j and arr[i]!=k:
        #     return None
        if i==j and arr[i]!=k:
            return -1
        mid=(i+j)/2
        temp=arr[mid]
        if k==arr[mid]:
            return mid
        if k>arr[mid]:
            i=mid+1
            res=self.binaryLooking(arr,i,j,k)
        else:
            j=mid-1
            res=self.binaryLooking(arr,i,j,k)
        return res