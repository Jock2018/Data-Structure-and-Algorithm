#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2019/5/7 9:01

@author: Jock
"""


def hell_sort(collection):
    length = len(collection)
    gap = length // 2
    while gap > 0:
        for i in range(0, gap):
            j = i + gap
            while j < length:
                k = j - gap
                temp = collection[j]
                while k >= 0 and collection[k] > temp:
                    collection[k + gap] = collection[k]
                    k -= gap
                collection[k + gap] = temp
                j += gap
        gap //= 2
    return collection

if __name__ == '__main__':
    collection = list(map(int, input().split()))
    print('排序前：', end='')
    for i in collection:
        print(i, end=' ')
    collection = hell_sort(collection)
    print('\n排序后：', end='')
    for i in collection:
        print(i, end=' ')