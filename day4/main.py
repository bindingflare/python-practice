# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:19:18 2020

@author: user
"""

class Manager:
    def __init__(self):
        self.students = []
    
    def add(self, student):
        self.students.append(student)

    def printStd(self):
        for student in self.students:
            student.printInfo()
            
            print()
            
    def dStudent(self, stdID):
        std = self.fStudent(stdID)
        
        if(std != None):
            self.students.remove(std)
                
    def fStudent(self, stdID):
        for student in self.students:
            if (student.getID() == stdID):
                return student
        
        return None

        
class Student:
    def __init__(self, name, stdID, math, kor, eng):
        self.name = name
        self.stdID = stdID
        self.math = math
        self.kor = kor
        self.eng = eng
    
    def avg(self):
        return (self.math + self.eng + self.kor) / 3
    
    def printInfo(self):
        print("Student details_")
        print("Name: %s ID: %s" % (self.name, self.stdID))
        
        print("Scores_")
        print("Math: %d Eng: %d Kor: %d" % (self.math, self.eng, self.kor))
        print("Average: %f" % (self.avg()))

    def getID(self):
        return self.stdID
    
    def getName(self):
        return self.name
        
class MainDriver:
    def __init__(self, manager):
        self.manager = manager
    
    def run(self):
        while True:
            self.printInstructions()
            x = int(input())
            
            if (x == 1):
                # 1 - add student
                std = self.inputStudent()
                
                print()
                
                manager.add(std)
            
            elif (x == 2):
                # 2 - remove student
                stdID = input("Input student ID: ")
                
                print()
                
                manager.dStudent(stdID)
            
            elif (x == 3):
                # 3 - edit student
                print("Input student ID: ")
                stdID = input()
                
                print()
                
                oldStd = manager.fStudent(stdID)
                
                if(oldStd == None):
                    print("Student not found. Please try again")
                else:
                    math = int(input("Input math: "))
                
                    eng = int(input("Input english: "))
                
                    kor = int(input("Input korean: "))
                    
                    print()
                
                    newStd = Student(oldStd.getName(), oldStd.getID(), math, eng, kor)
                
                    manager.dStudent(oldStd)
                    manager.add(newStd)
                
            elif (x == 4):
                # 4 - print student
                stdID = input("Input student ID: ")
                
                print()
                
                std = manager.fStudent(stdID)
                
                if(std == None):
                    print("Student not found. Please try again")
                else:
                    std.printInfo()
                
            elif (x == 5):
                # 5 - print all students
                print()
                manager.printStd()
                
            elif(x == 6):
                # 6 - exit
                print("Program will exit")
                break
        
    def printInstructions(self):
        print("Welcome to student management portal")
        print()
        print("Choose an option")
            
        print()
        print("1 - add student")
        print("2 - remove student")
        print("3 - edit student")
        print("4 - print student info")
        print("5 - print all student info")
        print("6 - exit")
        
    def inputStudent(self):
        name = input("Input name: ")
        
        stdID = input("Input student ID: ")
        
        math = int(input("Input math score: "))
        
        eng = int(input("Input english score: "))
        
        kor = int(input("Input korean score: "))
        
        return Student(name, stdID, math, eng, kor)

if __name__ == "__main__":
    manager = Manager()
    p = MainDriver(manager)
    p.run()