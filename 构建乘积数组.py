# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        B=[0]*len(A)
        B[0]=self.getMul(A[1:])
        for i in range(1,len(A)):
            left=right=1
            if len(A[:i])>0:
                left=self.getMul(A[:i])
            if len(A[i+1:])>0:
                right=self.getMul(A[i+1:])
            B[i]=left*right
        return B
    def getMul(self,l):
        return reduce(lambda x,y:x*y,l)
        '''
       利用b[i]=b[i-1]*a[i-1]/a[i]实现
        length=len(A)
        B=[0]*length
        B[0]=reduce(lambda x,y:x*y,A[1:])
        for i in range(1,length):
            B[i]=self.division(B[i-1]*A[i-1],A[i])
        return B
    def division(self,a, b):
	    if(b==0):
		    return 0;
	    flag = True;
	    if(self.getsign(a) == self.getsign(b)):# //积的符号判定
		    flag = False;
	    a = self.bepositive(a);
	    b = self.bepositive(b);
	    n = 0;
	    a = self.subtraction(a, b);
	    while(a>=0):
		    n = self.add(n, 1);
		    a = self.subtraction(a, b);
	    if(flag):
		    n = self.negtive(n);
	    return n;

    def getsign(self,i):# //取一个数的符号，看是正还是负
	    return (i>>31);
    
    def bepositive(self, i) :#//将一个数变为正数，如果本来就是正，则不变；如果是负，则变为相反数。注意对于-2147483648，求负会溢出。
	    if(i>>31):
		    return self.negtive(i);
	    else:
		    return i;
    def negtive(self, i):
	    return self.add(~i, 1);
    def  subtraction(self, a,  b):# //减法运算：利用求负操作和加法操作
	    return self.add(a, self.negtive(b));
    def add(self,a,b):
	    s=c=0
	    while(b != 0):
		    s = a^b;
		    c = (a&b)<<1;
		    a = s;
		    b = c;
	    return a;
        '''