#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-09-28.


def bubble_sort(array):
    length = len(array)

    for i in range(length - 1, -1, -1):

        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


print(bubble_sort([123, 31, 1231414, 3214, 123, 4, 231]))
