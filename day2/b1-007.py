# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 16:15:20 2020

@author: user
"""

print("Input height", end = '')
height = int(input())

row = 1
for i in range(height):
    num = row
    
    for j in range(height):
        print("%d " % num, end = '')
        num = num + height
    
    print()
    row += 1