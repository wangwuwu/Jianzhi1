# -*- coding:utf-8 -*-
import math
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent==0:
            return 1
        if base==0:
            return 0
        elif exponent>0:
            return base*self.Power(base,exponent-1)
        else:
            exponent=int(math.fabs(exponent))
            return 1/(base*self.Power(base,exponent-1))