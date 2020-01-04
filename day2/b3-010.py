# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 18:30:02 2020

@author: user
"""

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def setData(self, first, second):
        self.first = first
        self.second = second
        
    def add(self):
        return self.first + self.second
    def sub(self):
        return self.first - self.second
    def mul(self):
        return self.first * self.second
    def div(self):
        return self.first / self.second

class MoreFourCal(FourCal):
    pass

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:  # Add safety for divide 0 error
            return 0
        else:
            return self.first / self.second

a = FourCal(4, 2)
a.setData(4,2)
print(a.first)
print(a.second)
print(id(a.first))
print(id(a.second))

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

a = MoreFourCal(4,2)
print(a.add())