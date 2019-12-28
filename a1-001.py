# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 16:24:55 2019

@author: user
"""

# 홍길동 씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해 보자.

subjects = ["국어", "영어", "수학"]
scores = [80, 75, 55]

total = 0
count = 0

for i in scores:
    total = total + i
    count += 1

total = total / count

print("Average of %d subjects: %d" % (count , total))