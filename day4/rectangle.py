# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:39:20 2020

@author: user
"""

class Rectangle:
    def __init__(self, x, y , w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
    def show(self):
        print("%d %d %d %d" % (self.x, self.y, self.w, self.h))
        
    def square(self):
        return self.w * self.h
        
    def contains(self, other):
        if(other.x >= self.x and other.y >= self.y):
            if((other.x + other.w) < (self.x + self.w) and (other.y + other.h) < (self.y + self.h)):
                return True
        return False
    

if __name__ == "__main__":
    r = Rectangle(2, 2, 8, 7)
    s = Rectangle(5, 5, 6, 6)
    t = Rectangle(1, 1, 10, 10)
    
    r.show()
    print("s area: " + str(s.square()))
    
    if(t.contains(s)):
        print("t contains s")
    if(t.contains(r)):
        print("t contains r")