#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-09-28.


def insert_sort(array):
    for i in range(1, len(array), 1):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1

    return array


print(insert_sort([3123, 312, 312, 34, 123, 4, 1234, 23, 4, 325, 12345, 34, 5]))
