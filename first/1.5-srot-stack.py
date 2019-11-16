#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-11-16.


def sortstack(stack):
    help_stack = []

    while stack:

        item = stack.pop()

        if not help_stack:
            help_stack.append(item)

        else:

            help_head = help_stack[-1]
            while help_stack and item > help_head:
                stack.append(help_stack.pop())
                if help_stack:
                    help_head = help_stack[-1]

            help_stack.append(item)

    while help_stack:
        stack.append(help_stack.pop())


a = [1, 432, 4321, 2, 234, 35, 1, 2]

sortstack(a)

print(a)
