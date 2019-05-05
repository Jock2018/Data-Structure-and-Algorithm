#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2019/5/5 16:51

@author: Jock
"""

import random


def quick_sort_random_pivot(collection, low, high):
    # 快速排序
    if low >= high:
        return collection
    else:
        rand = random.randint(low, high)
        collection[rand],collection[low] = collection[low], collection[rand]    # 随机取一个作为基准值
        pivot = collection[low]
        left = low
        right = high
        while left < right:
            while left < right and collection[right] >= pivot:
                right -= 1    # 右边的哨兵左移一个
            collection[left] = collection[right]
            while left < right and collection[left] <= pivot:
                left +=1    # 左边的哨兵右移一个
            collection[right] = collection[left]
        collection[right] = pivot    # 两个哨兵相遇时则说明找到基准值的位置
        quick_sort_random_pivot(collection, low, left-1)    # 递归左半部分
        quick_sort_random_pivot(collection, left+1, high)    # 递归右半部分
        return collection

if __name__ == '__main__':
    collection = list(map(int, input().split()))
    print('排序前：', end='')
    for i in collection:
        print(i, end=' ')
    collection = quick_sort_random_pivot(collection, 0, len(collection)-1)
    print('\n排序后：', end='')
    for i in collection:
        print(i, end=' ')