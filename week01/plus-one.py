#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/11/21 8:21 下午
# @Author  : Focus
# @software: PyCharm
"""
加一
"""

class Solution:
    def plusOne(self, digits):
        cur = len(digits)
        while True:
            if digits[cur - 1] != 9:
                digits[cur - 1] += 1
                return digits
            else:
                digits[cur - 1] = 0
                cur -= 1
                if cur - 1 < 0:
                    return [1] + digits