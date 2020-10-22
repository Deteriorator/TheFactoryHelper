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
                # print('{:<20}{:<8.2f}{:<8}{:<2.2f}'.format(k, self.staple_cost(k), v, self.staple_cost(k) * v))
                cost += self.staple_cost(k) * v
            if k in Config.ManuFacturing:
                cost += self.product_cost(k) * v
        return cost

    def product_profit(self, item) -> float:
        price = self.product.get(item).get('price')
        profit = price - self.product_cost(item)
        return profit

    def product_profit_rate(self, item) -> float:
        return round(self.product_profit(item) / self.product_cost(item), 2)

    def update_dict(self):
        ordered_product = []
        for k, v in self.product.items():
            info = {}
            info['Name'] = k
            info['Cost'] = self.product_cost(k)
            info['ProfitRate'] = self.product_profit_rate(k)
            ordered_product.append(info)
        new = sorted(ordered_product, key=lambda a: a.get('ProfitRate'), reverse=True)
        # 'Adv concrete': {'Cost': 247.01, 'ProfitRate': 0.33}, 'Belt': {'Cost': 247.01, 'ProfitRate': 0.33},
        return new

    def profit_dict(self) -> dict:
        profit = {}
        for k, v in self.product.items():
            profit[k] = self.product_profit_rate(k)
        return profit

    def cost_dict(self) -> dict:
        cost = {}
        for k, v in self.product.items():
            cost[k] = self.product_cost(k)
        return cost
