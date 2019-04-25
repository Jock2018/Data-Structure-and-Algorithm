#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2019/4/25 8:13

@author: Jock
"""


def bubble_sort(collection):
    length = len(collection)
    for i in range(length-1):    # 只要冒泡length-1轮就可以排好序
        swapped = False    # 记录是否发生交换
        for j in range(length-1-i):
            if collection[j] > collection[j+1]:
                swapped = True
                collection[j], collection[j+1] = collection[j+1], collection[j]
        if  not swapped:    # 没有发生交换，如果已经排好序
            break
    return collection

if __name__ == '__main__':
    collection = list(map(int, input().split()))
    print('排序前：', end='')
    for i in collection:
        print(i, end=' ')
    collection = bubble_sort(collection)
    print('\n排序后：', end='')
    for i in collection:
        print(i, end=' ')
