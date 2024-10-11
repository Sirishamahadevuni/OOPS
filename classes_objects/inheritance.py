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
# class Parent:
#     def method1(self):
#         print("I am parent")
# class child(Parent):
#     def method2(self):
#         print("i'm child")
# child1=child()
# child1.method2()
# child1.method1()  

# MULTIPLE INHERITANCE
class Father:
    def method3(self):
        print("im a father")
class Mother:
    def method3(self):
        print("im a mother")
class Child(Father,Mother):
    def method4(self):
        print("im a child")
child1=Child()
child1.method4()
child1.method3()

""" 
While inheriting if we have 2 or more methods with same name then we use the "MRO"--METHOD RESOLUTION ORDER
It checks for methods in child first then it goes in  order that mentioned 
"""