#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-11-15.


def hannuo(n, _from, _to, _help):
    if n == 1:
        print(f"move {n} from {_from} to {_to}")

    else:

        hannuo(n - 1, _from, _help, _to)
        print(f"move {n} from {_from} to {_to}")
        hannuo(n - 1, _help, _to, _from)


hannuo(3, "左", "右", "中")


def xx(marx, i, j):
    if i == len(marx) - 1 and j == len(marx[0]) - 1:
        return marx[i][j]

    else:
        if i == len(marx) - 1:
            return marx[i][j] + xx(marx, i, j + 1)

        elif j == len(marx[0]) - 1:
            return marx[i][j] + xx(marx, i + 1, j)
        else:
            return marx[i][j] + min(
                xx(marx, i + 1, j)
                , xx(marx, i, j + 1)
            )
        编写代码



def find(ffdsafdsaledsafsa):


    pass







