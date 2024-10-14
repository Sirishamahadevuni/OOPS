""" instance methods:Generally the methods we create in class are instance methods--to perform operations 
on instance variables we create instance methods--objects
accessed through objects,reference:self


class method:To perform operations on class level variables we create class methods and deal with factory methods
accessed through both class and objects,reference:cls

static methods:general methods,to perform general task--doesnt perform operations on objects and class variables
accessed through: class and objects , there is no need for reference

static method is called as utility Function

only do related geneeral task for which the class is created

example:calculator app
methods:add,sub,mult,division
"""
class calculator:
    
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def sub(a,b):
        return a-b
    @staticmethod
    def mul(a,b):
        return a*b
    @staticmethod
    def div(a,b):
        return a/b
print(calculator.add(3,5))
print(calculator.sub(18,5))
print(calculator.mul(33,5))
print(calculator.div(30,5))