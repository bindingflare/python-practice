# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 17:43:55 2019

@author: user
"""

# 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다. 다음과 같이 a, b
# 변수를 선언한 후 a의 두 번째 요솟값을 변경하면 b 값은 어떻게 될까? 그리고 이런
# 결과가 오는 이유에 대해 설명해 보자.

a = b = [1, 2, 3]
a[1] = 4
print(b)

# a와 b는 똑같은 list를 저장하고 있으나 실제로 list의 위치를 동일하게 저장하고있다.
# 따라서 a를 통해 변경한 list는 b에도 나타난다.