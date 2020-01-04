# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 16:32:55 2020

@author: user
"""

print("Input height, length", end = '')
height, length = map(int,input().split(' '))


print("Choose option [1 ~ 3]")
option = int(input())

if option == 1:
    for i in range(1, height + 1):
        print("%d " % i * length)

elif option == 2:
    change = 1
    
    for i in range(height):
        if change == 1:
            j = 1
            end = length
        else:
            j = length
            end = 1
        
        while j != end:
            print("%d " % j, end = '')
            j += change
            
            if j == end:
                print(j, end = '')
        
        print()
        change *= -1

elif option == 3:
    change = 1
    
    for i in range(1, height + 1):
        start = i
        j = 0
        
        while j < length:
            print("%d " % start, end = '')
            start += change
            j += 1
        
        print()
        change += 1;