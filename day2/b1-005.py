# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 15:38:34 2020

@author: user
"""

input_str = input("Input height, length\n")

height, length = input_str.split(' ')
length = int(length)
height = int(height)

count = 1
for i in range(height):
    for j in range(length):
        print("%d " % count, end = '')
        count += 1
    print()