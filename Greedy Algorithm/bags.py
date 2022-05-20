# -*- coding: utf-8 -*-
"""
贪婪法例子：假设小偷有一个背包，最多能装20公斤赃物，他闯入一户人家，发现如下表所示的物品。
很显然，他不能把所有物品都装进背包，所以必须确定拿走哪些物品，留下哪些物品。

名称	价格（美元）	重量（kg）
电脑	200	20
收音机	20	4
钟	175	10
花瓶	50	2
书	10	1
油画	90	9
"""


class Thing(object):
    """物品"""

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        """价格重量比"""
        return self.price / self.weight

if __name__ == '__main__':
    a = Thing("tom",20,10)
    print(a.value)