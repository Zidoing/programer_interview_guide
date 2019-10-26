#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-10-19.


array = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18]
]


def hui_print(array):
    if len(array) == 0:
        return

    start_r = 0
    start_c = 0
    end_r = len(array) - 1
    end_c = len(array[0]) - 1

    while (start_r <= end_r and start_c <= end_c):
        xx_print(array, start_r, start_c, end_r, end_c)
        start_r += 1
        start_c += 1
        end_r -= 1
        end_c -= 1


def xx_print(array, start_r, start_c, end_r, end_c):
    if start_r == end_r:

        while (start_c <= end_c):
            print(array[start_r][start_c])
            start_c += 1

    elif start_c == end_c:
        while (start_r <= end_r):
            print(array[start_r][start_c])
            start_r += 1


    else:

        cur_r = start_r
        cur_c = start_c

        while cur_c < end_c:
            print(array[cur_r][cur_c])
            cur_c += 1

        while cur_r < end_r:
            print(array[cur_r][cur_c])
            cur_r += 1

        while cur_c > start_c:
            print(array[cur_r][cur_c])
            cur_c -= 1

        while cur_r > start_r:
            print(array[cur_r][cur_c])
            cur_r -= 1


hui_print(array)
