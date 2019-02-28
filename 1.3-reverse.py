#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-02-27.
# 如何使用递归函数和栈操作逆序一个栈


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

stack.push(1)
stack.push(2)
stack.push(23)
stack.push(12)
stack.push(5)
stack.push(9)

print(stack)


def get_last_element_and_remove(stack):
    result = stack.pop()

    if not stack:
        return result

    last = get_last_element_and_remove(stack)

    stack.push(result)

    return last


def reverse(stack):
    if not stack:
        return

    last = get_last_element_and_remove(stack)

    reverse(stack)
    stack.push(last)
