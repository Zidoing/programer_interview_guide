#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-02-27.
## 由2个栈组成的队列
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


class TwoStackQueue:

    def __init__(self):
        self.push_stack = Mystack()
        self.pop_stack = Mystack()

    def add(self, value):
        self.push_stack.push(value)

    def poll(self):

        if not self.pop_stack and self.push_stack:
            while True:
                data = self.push_stack.pop()
                if data:
                    self.pop_stack.push(data)
                else:
                    break
        elif not self.pop_stack and not self.push_stack:
            return None

        return self.pop_stack.pop()

    def peek(self):
        if self.pop_stack:
            return self.pop_stack.stackData[-1]
        if not self.pop_stack and not self.push_stack:
            return None

        while True:
            data = self.push_stack.pop()
            if data:
                self.pop_stack.push(data)
            else:
                break

        return self.pop_stack.stackData[-1]


a = [10, 2, 3, 4, 52, 1, 2, 3]

queue = TwoStackQueue()

for item in a:
    queue.add(item)

print(queue.peek())

print("begin pop")
while True:

    data = queue.poll()
    if data:
        print(data)

    else:
        break
