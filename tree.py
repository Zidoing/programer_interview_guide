#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-10-27.


class Node:
    def __init__(self, val, ):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.val)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

node1.parent = None
node2.parent = node1
node3.parent = node1
node4.parent = node2
node5.parent = node2

node6.parent = node3
node7.parent = node3
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7


def preOrder(root):
    if root is None:
        return "#_"

    string = str(root.val) + "_"
    string += preOrder(root.left)
    string += preOrder(root.right)
    return string


node_string = preOrder(node1)


def recover_node(string):
    node_val = string.split("_")

    return recoverPreorder(node_val)


def recoverPreorder(node_val):
    if node_val:
        value = node_val.pop(0)
        if value == "#":
            return
        head = Node(value)
        head.left = recoverPreorder(node_val)
        head.right = recoverPreorder(node_val)

        return head





def preOrder2(root):
    stack = []

    stack.append(root)

    while stack:

        head = stack.pop()
        print(head.val)
        if head.right:
            stack.append(head.right)
        if head.left:
            stack.append(head.left)

preOrder2(recover_node(node_string))
print("sep")
# print('前序')
# preOrder(node1)
# print('------------')
preOrder2(node1)


def inOrder(root):
    if root is None:
        return

    inOrder(root.left)
    print(root.val)
    inOrder(root.right)


def inOrder2(root):
    stack = []
    head = root

    while head or stack:

        if head:
            stack.append(head)
            head = head.left

        else:
            head = stack.pop()

            print(head.val)

            head = head.right


def get_after(node):
    if node.right:
        head = node.right
        while head.left:
            head = head.left
        return head

    else:
        parent = node.parent

        while parent and parent.left != node:
            node = parent
            parent = node.parent

        return parent


def get_before(node):
    if node.left:
        head = node.left
        while head.right:
            head = head.right

        return head

    else:

        parent = node.parent

        while parent and parent.right != node:
            node = parent
            parent = node.parent

        return parent


print(get_before(node7))

print(get_after(node7))

print('中序')
inOrder(node1)


# print('------------')
# inOrder2(node1)


def posOrder(root):
    if root is None:
        return

    posOrder(root.left)
    posOrder(root.right)
    print(root.val)


def posOrder2(root):
    stack1 = []
    stack2 = []

    stack1.append(root)

    while stack1:
        head = stack1.pop()
        stack2.append(head.val)
        if head.left:
            stack1.append(head.left)
        if head.right:
            stack1.append(head.right)

    while stack2:
        print(stack2.pop())

#
# print('后序')
# posOrder(node1)
# print('------------')
# posOrder2(node1)
