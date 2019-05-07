#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2019/5/7 9:38

@author: Jock
"""


def hell_sort_optimization(collection):
    length = len(collection)
    gap = length // 2
    while gap > 0:
        j = gap
        while j < length:
            k = j - gap
            temp = collection[j]
            while k >= 0 and collection[k] > temp:
                collection[k + gap] = collection[k]
                k -= gap
            collection[k + gap] = temp
            j += 1
        gap //= 2
    return collection

if __name__ == '__main__':
    collection = list(map(int, input().split()))
    print('排序前：', end='')
    for i in collection:
        print(i, end=' ')
    collection = hell_sort_optimization(collection)
    print('\n排序后：', end='')
    for i in collection:
        print(i, end=' ')