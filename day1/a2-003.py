# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 16:34:07 2019

@author: user
"""

# 홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.

security_number = "881120-1068234"

year = int(security_number[0:2])
month = int(security_number[2:4])
day = int(security_number[4:6])

num = int(security_number[7:])

print(
"""Year: %d
Month: %d
Day: %d

Number: %d
""" % (year, month, day, num)
)