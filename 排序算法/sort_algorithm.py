# -*- coding: utf-8 -*-

def select_sort(items, comp=lambda x, y: x < y):
    """
    选择排序，外层for循环每次找到一个最小值
    """
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


def bubble_sort(items, comp=lambda x, y: x > y):
    """冒泡排序
    1、比较相邻的元素。如果第一个比第二个大，就交换它们两个。
    2、对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
    3、针对所有的元素重复以上的步骤，除了最后一个。
    4、持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
    """
    # items = items[:]
    # for i in range(len(items)-1):
    #     for j in range(1,len(items)-i):
    #         if comp(items[j-1],items[j]):
    #             items[j-1],items[j] = items[j],items[j-1]
    # return items

    # 增加一个优化项：如果在外层某一轮循环中，没有发生交换，说明已经有序，则停止循环。
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(1, len(items) - i):
            if comp(items[j - 1], items[j]):
                items[j - 1], items[j] = items[j], items[j - 1]
                swapped = True
        if not swapped:
            break
        print(i, items)
    return items


def cocktail_sort(items, comp=lambda x, y: x > y):
    """
    1、先对数组从左到右进行冒泡排序（升序），则最大的元素去到最右端；
    2、再对数组从右到左进行冒泡排序（降序），则最小的元素去到最左端；
    """
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:  # 如果从左到右发生了交换，则进行从右到左的冒泡排序
            for j in range(len(items) - 2 - i, i, -1):  # 可以取到len(items)-2-i，但是取不到len(items)-1-i
                if comp(items[j], items[j - 1]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
        print(i, items)
    return items


def merge(items1, items2, comp=lambda x, y: x < y):
    """合并(将两个有序的列表合并成一个有序的列表)"""
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):  # 将两个列表中的最小值添加到items
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    # while循环的推出条件：两个列表有一个的索引已经到了末位，此时把另一个列表剩余元素的添加到items
    items += items1[index1:]
    items += items2[index2:]
    return items


def _merge_sort(items, comp):
    """归并排序"""
    if len(items) < 2:
        return items
    mid = len(items) // 2
    left = _merge_sort(items[:mid], comp)
    right = _merge_sort(items[mid:], comp)
    return merge(left, right, comp)


def merge_sort(items):
    return _merge_sort(items, comp=lambda x, y: x < y)


if __name__ == '__main__':
    a = [1, 2, 10, 4, 3, 7, 6, 9, 8]
    r = merge_sort(a)
    print(r)