#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     config.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.10.19   23:50
-------------------------------------------------------------------------------
   @Change:   2020.10.19
-------------------------------------------------------------------------------
"""


class Config:

    Purchasing = [
        'Cardboard',
        'Concrete',
        'Magnet',
        'Metal',
        'Paint',
        'Plastic',
        'Rare metal',
        'Rubber',
        'Wire'
    ]

    ManuFacturing = {
        'Adv concrete': {
            'Concrete': 2,
            'Metal': 2
        },
        'Belt': {
            'Rubber': 2
        },
        'Box': {
            'Cardboard': 4
        },

    }
