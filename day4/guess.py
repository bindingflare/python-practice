# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:09:45 2020

@author: user
"""

from random import randint

if __name__ == "__main__":
    i = randint(1, 100)
    
    while True:
        pick = int(input("Pick a number: "))
        
        if(pick == i):
            break
        elif(pick < i):
            print("Higher!")
        else:
            print("Lower!")
    
    print("The lucky number was %d!" % i)