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
            'price': 15.90,
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

        'Air gun': {
            'price': 19.78,
            'part': {
                'Metal': 4,
                'Hose': 2
            }
        },
        'Arm': {
            'price': 51.68,
            'part': {
                'Metal': 2,
                'Circuit': 1,
                'Motor': 2
            }
        },
        'Conveyor': {
            'price': 102.58,
            'part': {
                'Belt': 1,
                'Gear': 2,
                'Metal wheel': 8,
                'Motor': 1
            }
        },
        'Lifter': {
            'price': 55.46,
            'part': {
                'Metal': 3,
                'Cable': 2,
                'Hose': 2,
                'Motor': 1,
                'Pump': 1
            }
        },
        'Logic unit': {
            'price': 26.75,
            'part': {
                'Wire': 5,
                'Circuit': 4
            }
        },
        'Mover': {
            'price': 113.65,
            'part': {
                'Metal': 3,
                'Gear': 4,
                'Metal wheel': 4,
                'Motor': 2
            }
        },
        'Road': {
            'price': 49.80,
            'part': {
                'Concrete': 4,
                'Adv concrete': 2
            }
        },
        'Support': {
            'price': 40.53,
            'part': {
                'Metal': 2,
                'Adv concrete': 2
            }
        },
        'Thing-a-ma-jig': {
            'price': 61.02,
            'part': {
                'Circuit': 3,
                'Hose': 2,
                'Motor': 1,
                'Pump': 2
            }
        },
        'Widget': {
            'price': 14.78,
            'part': {
                'Metal': 1,
                'Plastic': 4,
                'Wire': 2,
                'Circuit': 1
            }
        },
        'Toy car': {
            'price': 35.38,
            'part': {
                'Metal': 1,
                'Paint': 1,
                'Plastic': 3,
                'Plastic wheel': 4,
                'Box': 1
            }
        },
        'Water gun': {
            'price': 29.62,
            'part': {
                'Paint': 1,
                'Plastic': 6,
                'Hose': 2,
                'Box': 1
            }
        },
        'Adv logic unit': {
            'price': 87.15,
            'part': {
                'Wire': 4,
                'Circuit': 4,
                'Logic unit': 2
            }
        },
        'Assembly line': {
            'price': 715.84,
            'part': {
                'Air gun': 2,
                'Arm': 2,
                'Conveyor': 3,
                'Lifter': 1,
                'Mover': 1
            }
        },
        'Jet engine': {
            'price': 180.04,
            'part': {
                'Metal': 8,
                'Wire': 12,
                'Hose': 6,
                'Pump': 4,
                'Thing-a-ma-jig': 1
            }
        },
        'Sensor': {
            'price': 51.51,
            'part': {
                'Rare metal': 2,
                'Wire': 1,
                'Circuit': 1,
                'Logic unit': 1
            }
        },
        'Bridge': {
            'price': 1091.16,
            'part': {
                'Road': 6,
                'Support': 6
            }
        },
        'Forklift': {
            'price': 198.04,
            'part': {
                'Metal': 6,
                'Rubber': 8,
                'Metal wheel': 4,
                'Motor': 2,
                'Box': 4
            }
        },
        'Radio tower': {
            'price': 414.00,
            'part': {
                'Metal': 12,
                'Wire': 6,
                'Support': 4
            }
        },
        'Tablet computer': {
            'price': 93.14,
            'part': {
                'Plastic': 1,
                'Wire': 3,
                'Circuit': 3,
                'Logic unit': 1,
                'Box': 1
            }
        },
        'Builder:Tier 1': {
            'price': 328.74,
            'part': {
                'Motor': 1,
                'Arm': 2,
                'Conveyor': 1,
                'Thing-a-ma-jig': 1
            }
        }
    }
