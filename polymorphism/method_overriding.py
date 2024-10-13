""" Super class and sub class has same method.if we access the method in subclass then only subclass method is accessed 
without accessing superclass method

Already created a method in superclass then implementing same method in subclass with different logic and accessing 
subclass. if it overrides superclass method then it is called method overriding

Rules for method Overriding:
1.super class and subclass must be present (inheritance must be done between two classes)
2.Declare two classes with same method and same parameters
3.Logic must be different in methods to observe the method override
4.method override will done when we access the same method in subclass.if we access in superclass than method will not override
if we change super class then the derived classes will also changes but we need method override in particular sub class 
so we have to call object from child class

class superclass:
    //same method
class subclass(superclass):
    //same method
"it follows mro "method resolution order"
"""
class grandparent:
    def method(self):
        print("this is grand parent method")
class parent(grandparent):
    def method(self):
        print("parent class method")
class child(parent):
    def method(self):
        print("this is child method")
obj1=child()
obj2=parent()
obj1.method()
obj2.method()
