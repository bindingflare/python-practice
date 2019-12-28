# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 18:27:05 2019

@author: user
"""

# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.

# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

# for문을 사용하여 A 학급의 평균 점수를 구해 보자.

marks = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

total = 0
count = 0

for mark in marks:
    count += 1
    total += mark
    
print(total/count)