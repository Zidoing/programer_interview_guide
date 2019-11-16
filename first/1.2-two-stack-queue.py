#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-02-27.
## 由2个栈组成的队列
from collections import deque


class Mystack:
    pass


class TwoStackQueue:
    stack = []
    help = []

    def add(self, item):
        self.stack.append(item)

    def poll(self):
        if not self.stack and not self.help:
            return None
        if self.help:
            return self.help.pop()
        else:
            while self.stack:
                self.help.append(self.stack.pop())
            return self.help.pop()

    def peek(self):
        if not self.stack and not self.help:
            return None
        if self.help:
            return self.help[-1]
        else:
            while self.stack:
                self.help.append(self.stack.pop())
            return self.help[-1]


a = TwoStackQueue()

a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(6231)

print(a.stack)
print(a.help)
print(a.poll())
print(a.poll())
print(a.poll())
print(a.poll())
print(a.poll())
