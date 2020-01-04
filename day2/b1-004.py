# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 15:04:31 2020

@author: user
"""

GUGDAN_MAX_NUMBER = 13

input_str = input("Input two numbers\n")

start, end = input_str.split(' ')
start = int(start)
end = int(end)

change = 1
if(start > end):
    change = -1

for i in range(start, end + change, change):
    for j in range(GUGDAN_MAX_NUMBER):
        print("%d x %d = %d" % (i, j, i * j))
    print();
