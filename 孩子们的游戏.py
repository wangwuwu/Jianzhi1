# -*- coding:utf-8 -*-
'''
每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,自然也准备了一些小游戏。其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)'''
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        '''
        使用数组来模拟环，当达到数组最后一个数后，索引置0，同时对于已经出列的数在数组中不删除，而是用-1代替（java版可以通过，python显示超时）
        l=[i for i in range(n)]
        i=-1#在l中的位置
        step=0#在m中的位置
        counts=n#l中还在的儿童数
        if n<0 or m<0:
            return -1
        while counts>0:
            i+=1
            if i>=n:
                i=0
            if l[i]==-1:
                continue
            step+=1
            if step==m:
                l[i]=-1
                step=0
                counts-=1
        return i
        '''
        if(n<1 or m<1):
            return -1;
        last=0;
        for i in range(2,n+1):
            last=(last+m)%i
        return last;