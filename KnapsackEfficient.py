# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 08:51:32 2017

@author: Yonarp
"""

import numpy as np

path = "knapsack_big1.txt"

with open(path) as file:
        knapsack_size,number_of_items = map(int,file.readline().strip().split())

        ks = knapsack_size
        ni = number_of_items

        items = np.empty([ni,2])

        for i,item in enumerate(file):
            items[i] = list(map(int,item.strip().split()))