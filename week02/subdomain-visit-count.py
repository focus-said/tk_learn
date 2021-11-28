#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/11/28 7:55 下午
# @Author  : Focus
# @software: PyCharm
"""
子域名访问计数
"""


class Solution:
    def subdomainVisits(self, cpdomains):
        result = {}
        return_list = []
        for s in cpdomains:
            tnum, tstr = s.split(' ')
            while True:
                if tstr in result:
                    result[tstr] += int(tnum)
                else:
                    result[tstr] = int(tnum)
                tmp = tstr.split('.', 1)
                if len(tmp) < 2:
                    break
                tstr = tmp[1]
        for k, v in result.items():
            return_list.append(str(v) + ' ' + k)
        return return_list


if __name__ == '__main__':
    test = ["9001 discuss.leetcode.com"]
    need_out = ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
    s = Solution()
    print(s.subdomainVisits(test))