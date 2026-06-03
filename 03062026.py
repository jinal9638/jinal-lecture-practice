#object oriented programming (oop)
'''
OOP is programming paradigm that organize code using classes and objects.
it helps in creating resuable,maintainable and scalable application
'''
#1.CLASS AND OBJECT
#A CLASS IS A BLUEPRINT OR TEMPLATE FOR CREATING OBJECT
#AN OBJECT  IS AN INSTANCE OF A CLASS
#STUDENT CLASS

class Student:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

#creating objects

s1=Student("Vivek",26)
s2=Student("Rahul",26)
s3=Student("Ronak",26)

print(s1)

s1.display()
s2.display()
s3.display()

#self keyword
#self represent that current object of the class
#instance variables/methods
#Employee

class Employee:

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def show(self):
        print("Employee Name:",self.name)
        print("Salary:",self.salary)

e1=Employee("Rahul",50000)
e1.show()

#del keyword
#delete variables,objects,object properties
'''
x=100
del x
print(x)
'''

#student

class  Student:

    def __init__(self):
        self.name="Vivek"

s1=Student()
'''
del s1

del s1.name
'''

#Encapsulation
'''

Encapsulation means wrapping object(data) and function(methods) into a
single unit (class) and restricting direct acess to some data
'''

#uses-->public,protected,private members

#bank account

class BankAccount:

    def __init__(self):

        self.__balance=100000

    def deposit(self,amount):

        self.__balance += amount

    def withdraw(self,amount):

        self.__balance-=amount

    def get_balance(self):
        return self.__balance

acc1=BankAccount()
acc1.deposit(50000)
acc1.withdraw(20000)

print("Account Balance:",acc1.get_balance())

#polymorphism
'''
polymorphism mean one interface many forms
The same method behaves differently for different objects
'''
#method overriding

class Animal:

    def sound(self):
        print("Animal makes sound")

class Dog(Animal):

    def sound(self):
        print("Dog bow bow")

class Snake(Animal):

    def sound(self):
        print("Snake shss....shss..")

d=Dog()
s=Snake()

d.sound()
s.sound()

#same function different objects

class Car:

    def move(self):
        print("Car is running.")

class Plane:

    def move(self):
        print("Plane is flying.")

def action(vehicle):
    vehicle.move()

action(Car())
action(Plane())


#Abstraction
'''
abstraction mean hiding implementation details and showing only essential features.
Python provides abstraction using the abc module
'''

#vehicle

class vehicle():

    def start(self):
        pass

class Car(vehicle):

    def start(self):
        print("Car started.")

class Bike(vehicle):

    def start(self):
        print("Bike started.")

Car().start()
Bike().start()

#Inheritance
'''
Inheritance allows one class to acquire properties and method of another class
'''

#1.single inheritance

class parent:

    def show(self):
        print("Parent class")

class child(parent):
    pass

child().show()

#multi level inheritance

class GrandParent:

    def title(self):
        print("Grand Parent")

class Parent(GrandParent):
    
    def title1(self):
        print("Parent")

class Child(Parent):

    def title2(self):
        print("Child")

Child().title()
Child().title1()
Child().title2()

#multiple inheritance

class Father:

    def father_property(self):
        print("Car")

class Mother:

    def mother_property(self):
        print("Jewellery")
    
class  Child(Father,Mother):
    pass

Child().father_property()
Child().mother_property()

#Hierarchical Inheritance

class Parent:

    def display(self):
        print("Parent class")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

Child1().display()
Child2().display()

#Hybrid inheritance


class A:

    def showA(self):
        print("A class")

class B(A):

    def showB(self):
        print("B class")

class C(A):

    def showC(self):
        print("C class")

class D(B,C):

    def showD(self):
        print("D class")

D().showA()
D().showB()        
D().showC()
D().showD()
