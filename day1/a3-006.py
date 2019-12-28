# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 18:28:33 2019

@author: user
"""

#리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.

numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
#위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.
        
print(result)

# using list comprehension

result = [number * 2 for number in numbers if number % 2 == 1]

print(result)