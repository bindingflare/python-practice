# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 15:49:06 2020

@author: user
"""

print("Input height")
height = int(input())

for i in range(height):
    for j in range(i + 1):
        print("*", end = '')
    print()
    
print()

for i in range(height):
    # spaces
    for j in range(i):
        print(" ", end = '')
    # number
    j = height - i
    while j > 0:
        print("*", end = '')
        j -= 1
    print()

print()

count = 1;
for i in range(height):
    # spaces
    for j in range(height - i - 1):
        print(" ", end = '')
    
    # number
    j = 0
    while j < count:
        print("*", end = '')
        j += 1
    print()
    count += 2