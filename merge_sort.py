#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-09-28.


min_count = []


def merge(left: list, right: list):
    helper = []

    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            helper.append(left[i])

            for x in range(len(right) - j):
                min_count.append(left[i])
            i += 1
        else:
            helper.append(right[j])
            j += 1

    while i < len(left):
        helper.append(left[i])
        i += 1

    while j < len(right):
        helper.append(right[j])
        j += 1

    return helper


def merge_sort(array):
    if len(array) == 1:
        return array

    mid = len(array) // 2

    left = merge_sort(array[:mid])

    right = merge_sort(array[mid:])
    print(left, right)
    da = merge(left, right)
    return da


print(merge_sort(
    [1, 3, 4, 2, 5]))

print(min_count)
print(sum(min_count))
