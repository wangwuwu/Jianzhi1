# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        
        if not sequence or len(sequence)==0:
            return False
        lenght=len(sequence)
        for i in range(lenght):
            if sequence[i]>sequence[lenght-1]:
                break
        for j in range(i,lenght):
            if sequence[j]<sequence[lenght-1]:
                return False
        left=True
        if i>0:
            left=self.VerifySquenceOfBST(sequence[0:i])
        right=True
        if i<lenght-1:
            right=self.VerifySquenceOfBST(sequence[i:-1])
        return left and right
        '''

        if sequence==None or len(sequence)==0:
            return False
        length=len(sequence)
        root=sequence[length-1]
        # �ڶ������� ���� �������ڵ�С�ڸ��ڵ�
        for i in range(length):
            if sequence[i]>root:
                break
        # �������������������Ľڵ㶼���ڸ��ڵ�
        for j  in range(i,length):
            if sequence[j]<root:
                return False
        # �ж��������Ƿ�Ϊ������
        left=True
        if  i>0:
            left=self.VerifySquenceOfBST(sequence[0:i])
        # �ж� �������Ƿ�Ϊ������
        right=True
        if i<length-1:
            right=self.VerifySquenceOfBST(sequence[i:-1])
        return left and right
    '''
