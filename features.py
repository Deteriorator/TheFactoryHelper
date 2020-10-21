#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     features.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.10.21   22:52
-------------------------------------------------------------------------------
   @Change:   2020.10.21
-------------------------------------------------------------------------------
"""

from config import Config


class Production(object):

    def __init__(self, staple: dict, product: dict):
        self.product = product   # 产品
        self.staple = staple     # 原料

    def staple_cost(self, item) -> float:
        return self.staple.get(item)

    def product_cost(self, item) -> float:
        product = self.product.get(item).get('part')
        cost = float(0.00)
        for k, v in product.items():
            if k in Config.Purchasing:
                print('{:<20}{:<8.2f}{:<8}{:<2.2f}'.format(k, self.staple_cost(k), v, self.staple_cost(k) * v))
                cost += self.staple_cost(k) * v
            if k in Config.ManuFacturing:
                cost += self.product_cost(k) * v
        return cost

    def product_profit(self, item):
        price = self.product.get(item).get('price')
        profit = price - self.product_cost(item)
        return profit

    def product_profit_rate(self, item):
        return round(self.product_profit(item) / self.product_cost(item), 2)

