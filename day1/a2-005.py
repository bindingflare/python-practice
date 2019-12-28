# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 16:41:25 2019

@author: user
"""

# 다음과 같은 문자열 a:b:c:d가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해 보자.

str = "a:b:c:d"

print(str.replace(':', '#'))