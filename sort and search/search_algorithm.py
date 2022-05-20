# -*- coding: utf-8 -*-
def seq_search(items, key):
    """顺序查找"""
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1

def bin_search(items,key):
    """二分查找，对已经排好序的列表"""
    start,end = 0,len(items)-1
    while start < end:
        mid = (start+end)//2
        if key > items[mid]: # 如果大于中间值，则下一次迭代的起点为mid+1
            start = mid + 1
        elif key < items[mid]: # 如果小于中间值，则下一次迭代的起点为mid-1
            end = mid-1
        else:
            return mid
    return -1


if __name__ == '__main__':
    a = list(range(1,100,2))
    r = bin_search(a,21)
    print(r)
