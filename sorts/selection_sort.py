#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2019/4/24 8:55

@author: Jock
"""


def seletion_sort(collecion):
    # 选择排序
    length = len(collection)
    for i in range(length -1):    # 比较length-1轮就可以排好序
        least = i
        for j in range(i+1, length):
            if collection[j] < collection[least]:
                least = j
        collection[i], collection[least] = collection[least], collection[i]
    return collection

if __name__ == '__main__':
    collection = list(map(int, input().split()))
    print('排序前：', end='')
    for i in collection:
        print(i, end=' ')
    collection = selection_sort(collection)
    print('排序后：', end=' ')
    for i in collection:
        print(i, end=' ')

