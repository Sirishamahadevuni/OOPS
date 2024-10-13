""" one of the power concept of oop
the process of handling complecity by hiding unneccessary information from users is called abstraction
real lyf example:atm machine (we dont know internally but we know how to use)

Abstract classes:  we can use abstract classes for implementing abstraction
if a class contain one or more than one abstract method then it is called abstract class

Abstract Method: If the method is declared without implementation it is called abstract method  
we can not instatiate this abstract method we use abc module to create abstract method "ABC abstract method"property
normal method in abstract class is called as concrete method
we cannot create object for abstract class
we cannot directly create object for abstract class but we can inherit abstrract class and we can create object

abstract methods in abstract class must implement in subclass

abstract class is used as blueprint for another class:If a project has lot of classes and functions then we create abstract class 
and use the class by inheriting used at design level

if we want to define set of clases if the classes has common behaviour then we create abstract class 
and derive subclasses from it

when we craete classes,if the class have same methods and implemmentation is different then we create abstract class
example;religion (pray:but diff way)
"""
# class A:
#     def method(self):
#         pass
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("this is concrete method")
    @abstractmethod
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("method")
    def method3(self):
        print("methd3")
obj1=B()
obj1.method1()
obj1.method2()
obj1.method3()