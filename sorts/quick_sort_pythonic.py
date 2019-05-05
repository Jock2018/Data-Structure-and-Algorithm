#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2019/5/5 9:03

@author: Jock
"""


def quick_sort_pythonic(collection):
    # 快速排序
    length = len(collection)
    if length <= 1:
        return collection
    else:
        pivot = collection[0]    # 取第一个数作为基准值
        left = [element for element in collection[1:] if element <= pivot]
        right = [element for element in collection[1:] if element > pivot]
        return quick_sort_pythonic(left) + [pivot] + quick_sort_pythonic(right)

if __name__ == '__main__':
    collection = list(map(int, input().split()))
    print('排序前：', end='')
    for i in collection:
        print(i, end=' ')
    collection = quick_sort_pythonic(collection)
    print('\n排序后：', end='')
    for i in collection:
        print(i, end=' ')