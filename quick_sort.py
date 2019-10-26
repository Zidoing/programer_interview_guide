#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-10-01.


def quick_sort(array):
    if len(array) <= 1:
        return array

    first = array[0]
    l = quick_sort([i for i in array if i < first])
    r = quick_sort([i for i in array if i > first])
    mid = [i for i in array if i == first]
    return l + mid + r


print(quick_sort([23321, 131, 1312243, 4112, 312, 312]))


def partition(array, num):
    less = -1
    cur = 0

    while cur < len(array):
        if array[cur] < num:
            less += 1
            array[cur], array[less] = array[less], array[cur]
            cur += 1
        else:
            cur += 1

    # for index, item in enumerate(array):
    #     if item < num:
    #         less += 1
    #         array[less], array[index] = array[index], array[less]
    print(less)
    return array


def partitions(array, num):
    less = -1
    more = len(array)

    cur = 0

    while cur < more:

        if array[cur] < num:
            less += 1
            array[less], array[cur] = array[cur], array[less]
            cur += 1
        elif array[cur] > num:
            more -= 1
            array[more], array[cur] = array[cur], array[more]
        else:
            cur += 1
    return array


print(partition(array=[3, 1, 4, 30, 2, 6, 31, 8, 30, 4, 6, 83, 23], num=30))
print(partitions(array=[3, 30, 4, 30, 2, 6, 31, 8, 30, 4, 6, 83, 23], num=30))
