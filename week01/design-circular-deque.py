#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/11/21 8:59 下午
# @Author  : Focus
# @software: PyCharm
class MyCircularDeque:

    def __init__(self, k: int):
        self.max = k
        self.deque = []
        self.length = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque = [value] + self.deque
        self.length += 1
        return True


    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque.append(value)
        self.length += 1
        return True


    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.deque = self.deque[1:]
            self.length -= 1
            return True
        return False


    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.deque.pop()
            self.length -= 1
            return True
        return False


    def getFront(self) -> int:
        if not self.isEmpty():
            return self.deque[0]
        return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.deque[-1]
        return -1


    def isEmpty(self) -> bool:
        if self.length > 0:
            return False
        return True

    def isFull(self) -> bool:
        if self.length < self.max:
            return False
        return True

