# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 14:56:42 2020

@author: user
"""

GUGUDAN_NUMBER = 3

terms = int(input("Input a number\n"))

n = 0;

for i in range(terms + 1):
    print("%d x %d = %d" % (GUGUDAN_NUMBER, n, GUGUDAN_NUMBER * n))
    n += 1