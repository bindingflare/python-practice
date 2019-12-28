# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 18:18:46 2019

@author: user
"""

# while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.

a = 3
step = a
total = 0

while a < 1000:
    #print(a)
    total += a
    a += step
    
print(total)