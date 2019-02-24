#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-02-24.
# 设计一个又getMin功能的栈

from collections import deque


class Mystack:
    stackData = deque()
    stackMin = deque()

    def push(self, num):

        if len(self.stackData) == 0:
            self.stackMin.append(num)

        elif num <= self.stackMin[-1]:
            self.stackMin.append(num)

        elif num > self.stackMin[-1]:
            self.stackMin.append(self.stackMin[-1])

        self.stackData.append(num)

    def pop(self):
        if len(self.stackData) == 0:
            return None
        pop_data = self.stackData.pop()

        self.stackMin.pop()

        return pop_data

    def get_min(self):

        if not self.stackMin:
            return None

        return self.stackMin[-1]


stack = Mystack()

stack.push(3)
stack.push(4)
stack.push(5)
stack.push(1)
stack.push(2)
stack.push(1)

print(stack.stackData)
print(stack.stackMin)

print(stack.get_min())

stack.pop()
print(stack.get_min())
stack.pop()
print(stack.get_min())
stack.pop()
print(stack.get_min())
stack.pop()
print(stack.get_min())
stack.pop()
print(stack.get_min())
stack.pop()
print(stack.get_min())
