# -*- coding:utf-8 -*-
'''
��ʵ��һ����������ƥ�����'.'��'*'��������ʽ��ģʽ�е��ַ�'.'��ʾ����һ���ַ�����'*'��ʾ��ǰ����ַ����Գ�������Σ�����0�Σ��� �ڱ����У�ƥ����ָ�ַ����������ַ�ƥ������ģʽ�����磬�ַ���"aaa"��ģʽ"a.a"��"ab*ac*a"ƥ�䣬������"aa.a"��"ab*a"����ƥ��
'''
class Solution:
    # s, pattern�����ַ���
    def match(self, s, pattern):

        if len(s) == 0 and len(pattern) == 0:
            return True
        # ���s��Ϊ�գ���patternΪ�գ���False
        elif len(s) != 0 and len(pattern) == 0:
            return False
        # ���sΪ�գ���pattern��Ϊ�գ�����Ҫ�ж�
        elif len(s) == 0 and len(pattern) != 0:
            # pattern�еĵڶ����ַ�Ϊ*����pattern������λ�����Ƚ�
            if len(pattern) > 1 and pattern[1] == '*':
                return self.match(s, pattern[2:])
            else:
                return False
        # s��pattern����Ϊ�յ����
        else:
            # pattern�ĵڶ����ַ�Ϊ*�����
            if len(pattern) > 1 and pattern[1] == '*':
                # s��pattern�ĵ�һ��Ԫ�ز�ͬ����s���䣬pattern������λ���൱��patternǰ��λ���ɿ�
                if s[0] != pattern[0] and pattern[0] != '.':
                    return self.match(s, pattern[2:])
                else:
                    # ���s[0]��pattern[0]��ͬ����pattern[1]Ϊ*�����ʱ�����������
                    # pattern����2����s���䣻�൱�ڰ�patternǰ��λ���ɿգ�ƥ������
                    # pattern����2����s����1�����൱��patternǰ��λ��s[0]ƥ��
                    # pattern���䣬s����1�����൱��patternǰ��λ����s�еĶ�λ����ƥ�䣬��Ϊ*����ƥ���λ
                    return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
            # pattern�ڶ����ַ���Ϊ*�����
            else:
                if s[0] == pattern[0] or pattern[0] == '.':
                    return self.match(s[1:], pattern[1:])
                else:
                    return False
        