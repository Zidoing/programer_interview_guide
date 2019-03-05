#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-03-05.
# 用一个栈实现另一个栈的排序
from builtins import sorted
from collections import deque


class Mystack:

    def __init__(self):
        self.stackData = deque()
        self.stackMin = deque()

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

    def peek(self):
        return self.stackData[-1]

    def __bool__(self):
        return bool(len(self.stackData))

    def __repr__(self):
        return "%s" % self.stackData


stack = Mystack()

stack.push(2)
stack.push(5)
stack.push(5)
stack.push(9)
stack.push(1)
stack.push(11)
stack.push(12)

print(stack)

print(sorted([2, 5, 5, 9, 1, 11, 12]))


def sort_stack_by_stack(stack: Mystack):
    help = Mystack()

    while stack:
        cur = stack.pop()

        if help and cur <= help.peek():
            help.push(cur)
        elif not help:
            help.push(cur)
        elif cur > help.peek():
            while help and cur > help.peek():
                stack.push(help.pop())

            help.push(cur)

    while help:
        stack.push(help.pop())


sort_stack_by_stack(stack)

print(stack)
