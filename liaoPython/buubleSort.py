#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
an implementation of bubble sort,
the least efficient sorting method
O(n**2)
'''

__author__ = 'Dong Wang'


def bubbleSort(L):
    length = len(L)
    for passNum in range(length-1, 0, -1):
        for position in range(passNum):
            if L[position] > L[position+1]:
                L[position], L[position + 1] = L[position + 1], L[position]
    return L

def shortBubbleSort(L):
    '''
    stop while detecting the rest of the list was already sorted
    '''
    passNum = len(L) - 1
    exchanged = True
    while passNum > 0 and exchanged:
        exchanged = False
        for i in range(passNum):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                exchanged = True
        passNum -= 1
    return L

if __name__ == '__main__':
    l1 = [54,26,93,17,77,31,44,55,20]
    l2 = []
    l3 = [53,26,93,17,77,31,44,55,20]

    print('Result1 of bubble sort:',bubbleSort(l1))
    print('Result2 of bubble sort:', bubbleSort(l2))
    print('Result1 of short bubble sort:', shortBubbleSort(l1))
    print('Result2 of short bubble sort:', shortBubbleSort(l3))
