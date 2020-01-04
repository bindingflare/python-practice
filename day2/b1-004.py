# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 15:04:31 2020

@author: user
"""

GUGDAN_MAX_NUMBER = 13

start = int(input("Input start number\n"))
end = int(input("Input end number\n"))

for i in range(start, end + 1):
    for j in range(GUGDAN_MAX_NUMBER):
        print("%d x %d = %d" % (i, j, i * j))
    print();