#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-11-16.


def getLastItem(stack):
    item = stack.pop()

    if not stack:
        return item
    else:
        last = getLastItem(stack)
        stack.append(item)

    return last



def reverse(stack):

    if not stack:
        return
    else:
        last = getLastItem(stack)


        reverse(stack)

        stack.append(last)


a = [1,2,3,4,5,6]
reverse(a)

print(a)
