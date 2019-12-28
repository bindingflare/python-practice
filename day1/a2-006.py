# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 16:42:24 2019

@author: user
"""

# [1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어 보자.

list = [1, 3, 5, 4, 2]

temp = 0;

temp = list[0]
list[0] = list[2]
list[2] = temp;

temp = list[1]
list[1] = list[3]
list[3] = temp

temp = list[2]
list[2] = list[3]
list[3] = temp

temp = list[3]
list[3] = list[4]
list[4] = temp

print(list)