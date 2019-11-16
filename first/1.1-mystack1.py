#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-11-16.


class MyStack:
    stack = []
    min_stack = []

    def pop(self):
        if not self.stack:
            return None
        self.stack.pop()
        self.min_stack.pop()

    def push(self, item):
        self.stack.append(item)
        if not self.min_stack:
            self.min_stack.append(item)

        else:
            if item < self.min_stack[-1]:
                self.min_stack.append(item)
            else:
                self.min_stack.append(self.min_stack[-1])

    def get_min(self):
        if not self.stack:
            return None
        return self.min_stack[-1]


stack = MyStack()

stack.push(3)
stack.push(4)
stack.push(5)
stack.push(1)
stack.push(2)
stack.push(1)

print(stack.stack)
print(stack.min_stack)

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
