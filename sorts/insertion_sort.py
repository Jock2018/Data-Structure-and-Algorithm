#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2019/4/24 8:53

@author: Jock
"""

def insertion_sort(collection):
    # 插入排序
    length = len(collection)
    for i in range(1, length):    # 第一个数作为初始有序序列，所以不用比较
        tmp = collection[i]
        j = i - 1
        while j >= 0 and collection[j] > tmp:
            collection[j+1], collection[j] = collection[j], tmp
            j -= 1
    return collection

if __name__ == '__main__':
    collection = list(map(int, input().split()))
    print('排序前是：', end='')
    for i in collection:
        print(i, end=' ')
    collection = insertion_sort(collection)
    print('\n排序后是：', end='')
    for i in collection:
        print(i, end=' ')
