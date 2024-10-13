""" Ability to use methods &attributes in newly created class from already created class is called inheritance
                or in simply we can say creating class from already created class
                
    already created class--super class,base class,parent class
    derived class--subclass,child cLass,derived class
    Types oof inheritance
    1.single inheriance--single class is used to create single class
    2.Multiple Inheritance--using more than 1 class to create single class
    3.Multilevel Inheritance
    4.Hierarchical inheritance
    5.Hybrd Inheritance   
"""
# SINGLE INHERITANCE
class Parent:
    def method1(self):
        print("I am parent")
class child(Parent):
    def method2(self):
        print("i'm child")
child1=child()
child1.method2()
child1.method1()  

