#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-10-04.


def heap_insert(array):
    for index, item in enumerate(array):
        while index > 0:
            father = (index - 1) >> 1
            if array[index] > array[father]:
                array[father], array[index] = array[index], array[father]
                index = father
            else:
                break


def heapfiy(array, index, heap_size):
    while index < heap_size:

        left = index * 2 + 1
        right = index * 2 + 2
        if left < heap_size:

            if right < heap_size:
                if array[right] > array[left]:
                    large = right
                else:
                    large = left

            else:
                large = left
            if array[index] < array[large]:

                array[index], array[large] = array[large], array[index]
            else:
                break
            index = large
        else:
            break


def heap_sort(array):
    heap_insert(array)

    length = len(array)

    while length > 1:
        array[0], array[length - 1] = array[length - 1], array[0]
        length = length - 1
        heapfiy(array, 0, length)


array = [2, 1, 3, 6, 0, 4]

heap_sort(array)

print(array)

#
# heap_insert(array)
# print(array)
# array = [1, 5, 4, 3, 5, 2]
# heapfiy(array, 0 ,6)
# print(array)
