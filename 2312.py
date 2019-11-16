#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-11-02.


def test():
    while True:
        return 1


test()


def is_full_tree(node):
    node_list = []

    node_list.append(node)

    leaf_mode = False
    while node_list:
        node = node_list.pop(0)

        left = node.left
        right = node.right

        if leaf_mode and (left is not None or right is not None) or (left is None and right is not None):
            return False

        if left:
            node_list.append(left)

        if right:
            node_list.append(right)

        if left is None or right is None:
            leaf_mode = True

        return True




