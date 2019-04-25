#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2019/4/25 9:09

@author: Jock
"""


def merge_sort(collection):
    # 归并排序
    length = len(collection)
    if length > 1:
        # 递归法完成第一步划分子表
        midpoint = length // 2    # 向上取整
        left_half = merge_sort(collection[:midpoint])
        right_half = merge_sort(collection[midpoint:])
        i = 0
        j = 0
        k = 0
        left_length = len(left_half)
        right_length = len(right_half)
        # 完成第二步，合并子表
        while i < left_length and j < right_length:
            if left_half[i] < right_half[j]:
                collection[k] = left_half[i]
                i += 1
            else:
                collection[k] = right_half[j]
                j += 1
            k += 1
        # 若左表有剩余，把左表剩余的数依次添加到合并表中
        while i < left_length:
            collection[k] = left_half[i]
            i += 1
            k += 1
        # 若右表有剩余，把右表的数依次添加到合并表中
        while j < right_length:
            collection[k] = right_half[j]
            j += 1
            k += 1
    return collection

if __name__ == '__main__':
    collection = list(map(int, input().split()))
    print('排序前：', end='')
    for i in collection:
        print(i, end=' ')
    collection = merge_sort(collection)
    print('\n排序后：', end='')
    for i in collection:
        print(i, end=' ')