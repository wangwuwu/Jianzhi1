'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0
'''
# -*- coding:utf-8 -*-
'''
二分查找的核心是，原数据有序（非递减），则旋转后第一个数据大于第二部分的所有数据，当一个数据大于arrau[0]时说明其肯定在第一部分中，则应当选取这个数据之后的部分
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
                i=mid#这里区别查找指定元素的mid+1
            elif rotateArray[mid]==rotateArray[i]:
                return rotateArray[mid+1]
            else:
                j=mid