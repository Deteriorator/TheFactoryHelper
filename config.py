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

    Purchasing = {
        'Cardboard': 0.24,
        'Concrete': 4.19,
        'Magnet': 5.68,
        'Metal': 3.40,
        'Paint': 2.26,
        'Plastic': 0.60,
        'Rare metal': 7.81,
        'Rubber': 1.10,
        'Wire': 1.71
    }

    ManuFacturing = {
        'Adv concrete': {
            'price': 14.47,
            'part': {
                'Concrete': 2,
                'Metal': 2
            }
        },
        'Belt': {
            'price': 2.6,
            'part': {
                'Rubber': 2
            }
        },
        'Box': {
            'price': 2.21,
            'part': {
                'Cardboard': 4
            }
        },
        'Cable': {
            'price': 3.28,
            'part': {
                'Metal': 1
            }
        },
        'Circuit': {
            'price': 3.54,
            'part': {
                'Plastic': 2,
                'Wire': 1
            }
        },
        'Gear': {
            'Price': 6.56,
            'part': {
                'Metal': 2
            }
        },
        'Hose': {
            'price': 2.6,
            'part': {
                'Rubber': 2
            }
        },
        'Metal wheel': {
            'price': 6.56,
            'part': {
                'Metal': 2
            }
        },
        'Motor': {
            'price': 17.40,
            'part': {
                'Magnet': 2,
                'Metal': 1,
                'Wire': 2
            }
        },
        'Plastic wheel': {
            'price': 1.72,
            'part': {
                'Plastic': 2
            }
        },
        'Pump': {
            'price': 8.72,
            'part': {
                'Metal': 2,
                'Plastic': 1,
                'Rubber': 1
            }
        },
        'Garden gnome': {
            'price': 15.9,
            'part': {
                'Concrete': 1,
                'Paint': 1,
                'Box': 1
            }
        },
        'Speakers': {
            'price': 29.42,
            'part': {
                'Magnet': 2,
                'Plastic': 2,
                'Wire': 1,
                'Box': 1
            }
        },
        'Toaster': {
            'price': 22.74,
            'part': {
                'Metal': 2,
                'Wire': 2,
                'Box': 1
            }
        },

    }
