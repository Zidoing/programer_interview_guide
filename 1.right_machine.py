#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-09-28.
import copy
import random

from bubble_sort import bubble_sort


def generateRandomArray(size, value):
    random_random = random.random()
    array = []

    for i in range(int((size + 1) * random_random)):
        array.append(int((value + 1) * random.random()))

    return array


def main_test():
    testTime = 50000
    size = 10
    value = 100
    succeed = True

    for i in range(testTime):
        source = generateRandomArray(size, value)
        arr1 = copy.copy(source)
        arr2 = copy.copy(source)

        bubble_sort(arr1)
        arr2.sort()

        if arr1 != arr2:
            print(source)
            print(arr1)
            print(arr2)

            succeed = False
            break

    if succeed:
        print("success")
    else:
        print("fail")


main_test()
