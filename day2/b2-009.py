# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 17:05:38 2020

@author: user
"""
# Q1
def is_odd(num): 
    return num % 2 == 1

print(is_odd(7))
print(is_odd(8))

# Q2
def average(*args):
    total = 0
    
    for num in args:
        total += num
    
    return total / len(args)

print(average(10, 20, 30, 40, 50))

# Q3
input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)

# Q4
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python") # prints spaces as well
print("".join(["you", "need", "python"]))

# Q5
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close() # Need to close to save

f2 = open("test.txt", 'r')
print(f2.read())

# Q6
f1 = open("test.txt", 'a')

gogo = True

while gogo:
    f1.write(input())
    
    print("Press any key to continue s to stop")
    if input() == 's':
        break

f1.close()

# Q7
#a = []

#f1 = open("test.txt", 'r')
#a.append(f1.readline().replace("java", "python"))
#f1.close()

#f2 = open("test.txt", 'w')
#for str in a:
#    f2.write(str + "\n")
#f2.close()

f = open("test.txt", 'r')

data = f.read()
f.close()

if "java" in data:
    data = data.replace("java", "python")

f = open("test.txt", 'w')
f.write(data)