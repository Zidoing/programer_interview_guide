#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-09-28.


def select_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i, len(array), 1):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]

    return array


print(select_sort([12321, 321, 2, 412, 4, 3124, 123, 412, 34, 123, 512, 5, 1235, 134, 5]))
