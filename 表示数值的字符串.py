# -*- coding:utf-8 -*-
import re
'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是
'''
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        '''
        直接匹配
        ^$表示从开始到结尾
        ?表示非贪婪模式，匹配一次或零次（可以用来表有或者没有）
        *匹配0次或多次
        +匹配至少一次
        8.和.8都是成立的
        '''
        
        return re.match(r"^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$",s)