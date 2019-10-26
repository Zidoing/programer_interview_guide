#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-10-05.


class Bucket:

    def __init__(self, m=None, M=None, is_empty=True):
        self.m = m
        self.M = M
        self.is_empty = is_empty

    def __repr__(self):
        return f"({self.m} | {self.M} | {self.is_empty})"


def max_sr(array):
    if len(array) <= 1:
        return 0

    buckets = [Bucket() for i in range(len(array) + 1)]

    m_value = 0
    M_value = 0

    m_value = min(array)
    M_value = max(array)

    if m_value == M_value:
        return 0

    split = (M_value - m_value) // (len(array) + 1)
    print(split)
    for num in array:

        index = int((num - m_value)* len(array) / (M_value - m_value) )

        if buckets[index].is_empty:
            buckets[index].m = num
            buckets[index].M = num
            buckets[index].is_empty = False

        else:
            buckets[index].m = min(num, buckets[index].m)
            buckets[index].M = max(num, buckets[index].M)

        print(buckets[index])
    res = 0

    pre_max = buckets[0].M
    print(buckets)
    for i in range(1, len(buckets)):
        if not buckets[i].is_empty:
            res = max(res, buckets[i].m - pre_max)
            pre_max = buckets[i].M
    return res


print(max_sr([15252,16764,27963,7817,26155,20757,3478,22602,20404,6739,16790,10588,16521,6644,20880,15632,27078,25463,20124,15728,30042,16604,17223,4388,23646,32683,23688,12439,30630,3895,7926,22101,32406,21540,31799,3768,26679,21799,23740]))
