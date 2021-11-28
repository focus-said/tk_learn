#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/11/28 8:13 下午
# @Author  : Focus
# @software: PyCharm
"""

"""

class Solution:
    def findShortestSubArray(self, nums):
        tmp = {}
        c = 0
        mim_num = 50000
        for index, x in enumerate(nums):
            if x in tmp:
                tmp[x]['end'] = index
                tmp[x]['c'] += 1
            else:
                tmp[x] = {'start': index, 'end': index, 'c': 1}
            if tmp[x]['c'] > c:
                mim_num = tmp[x]['end'] - tmp[x]['start'] + 1
                c = tmp[x]['c']
            elif tmp[x]['c'] == c:
                if (tmp[x]['end'] - tmp[x]['start'] + 1) < mim_num:
                    mim_num = tmp[x]['end'] - tmp[x]['start'] + 1
                    c = tmp[x]['c']
        return mim_num


if __name__ == '__main__':
    nums = [1,2,2,3,1,4,2]
    s = Solution()
    s.findShortestSubArray(nums)
