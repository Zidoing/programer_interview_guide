#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-11-08.


class UnionSet:
    father_map = {}
    size_map = {}

    def findHead(self, node):
        father = self.father_map.get(node)
        if father != node:
            father = self.findHead(father)

        self.father_map[node] = father
        return father

    def is_same_set(self, node_a, node_b):
        return self.findHead(node_a) == self.findHead(node_b)

    def union(self, node_a, node_b):
        a_head = self.findHead(node_a)

        a_head = self.findHead(node_b)

        b_head = self.findHead(node_b)

        size_a = self.size_map.get(a_head)
        size_b = self.size_map.get(b_head)

        if size_a > size_b:
            self.father_map[b_head] = a_head
            self.size_map[a_head] = size_b + size_a

        else:
            self.father_map[a_head] = b_head
            self.size_map[b_head] = size_b + size_a
