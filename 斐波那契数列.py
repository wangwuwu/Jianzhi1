# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        '''�ݹ����ʵ�֣�����ʱ�临�Ӷ�̫��
        if n==0:
            return 0
        if n==1:
            return 1
        else:
            return self.Fibonacci(n-1)+self.Fibonacci(n-2)
        '''
        '''
        ʹ������ʵ�֣���ÿһ���������һ��λ���ϣ�ÿһ��ֵ����ǰ����ֵ֮�ͣ�ʱ�临�Ӷ�Ϊn,�ռ临�Ӷ�Ϊn
        a=[0]*40
        a[0]=0
        a[1]=1
        if n==0|n==1:
            return n
        for i in range(2,n+1):
            a[i]=a[i-1]+a[i-2]
        return a[n]
        '''
        #ʱ�临�Ӷ�Ϊn ,�ռ临�Ӷ�Ϊ1
        one=0
        two=1
        three=0
        if n==0|n==1:
            return n
        for i in range(2,n+1):
            three=one+two
            one=two
            two=three
        return three