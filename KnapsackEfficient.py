# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 08:51:32 2017

@author: Yonarp
"""

import numpy as np
from scipy.ndimage.interpolation import shift
path = "knapsack1.txt"

with open(path) as file:
        knapsack_size,number_of_items = map(int,file.readline().strip().split())

        ks = knapsack_size
        ni = number_of_items

        items = np.empty([ni,2])

        for i,item in enumerate(file):
            items[i] = list(map(int,item.strip().split()))
#        for item in items:
#            print(item)
#        print("ks",ks)

        A = np.zeros([ks+1,2])
        A[:,0] = 0
        maxA = lambda x,y: max(x,y)
        maxArray = np.vectorize(maxA)
#        print (A)
        for i in range(1,ni+1):
#            print (A)
            temp1 = A[:,0]
#            print (temp1)
            temp2 = shift(A[:,0]+items[i-1,0],-int(items[i-1,1]),cval = 0)
#            print(temp2)
            A[:,1] = maxArray(temp1,temp2)
#            print(A)
            A[:,0] = A[:,1]
#            print(A)
#            if i is 5:
#                break
        print (A[0])